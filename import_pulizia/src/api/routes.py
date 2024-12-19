import ifcopenshell
import csv

def get_element_location(element):
    """
    Estrae le coordinate X, Y, Z dell'elemento IFC.
    
    :param element: Elemento IFC
    :return: Tuple delle coordinate (X, Y, Z) o ('N/A', 'N/A', 'N/A') se non disponibili
    """
    try:
        placement = element.ObjectPlacement
        if placement:
            return extract_location(placement)
    except Exception as e:
        print(f"Errore nell'estrazione della posizione per l'elemento {element.GlobalId}: {e}")
    return ('N/A', 'N/A', 'N/A')

def extract_location(placement):
    """
    Funzione ricorsiva per estrarre le coordinate dall'ObjectPlacement.
    
    :param placement: Oggetto di posizionamento IFC
    :return: Tuple delle coordinate (X, Y, Z)
    """
    coordinates = [0.0, 0.0, 0.0]
    
    while placement:
        if hasattr(placement, 'RelativePlacement'):
            relative = placement.RelativePlacement
            if relative and hasattr(relative, 'Location'):
                location = relative.Location
                if hasattr(location, 'Coordinates'):
                    coords = location.Coordinates
                    if isinstance(coords, list) or isinstance(coords, tuple):
                        coordinates[0] += coords[0]
                        coordinates[1] += coords[1]
                        coordinates[2] += coords[2]
        # Verifica se c'è una parent placement
        if hasattr(placement, 'PlacementRelTo'):
            placement = placement.PlacementRelTo
        else:
            break
    
    return tuple(coordinates)

def get_property_sets(element):
    """
    Ottiene tutti i Property Sets associati a un elemento IFC.
    
    :param element: Elemento IFC
    :return: Lista di IfcPropertySet
    """
    property_sets = []
    for definition in element.IsDefinedBy:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a("IfcPropertySet"):
                property_sets.append(property_set)
    return property_sets

def get_element_parameters(element):
    """
    Estrae tutti i parametri di un elemento IFC in un dizionario.
    
    :param element: Elemento IFC
    :return: Dizionario dei parametri
    """
    params = {}
    property_sets = get_property_sets(element)
    for pset in property_sets:
        for prop in pset.HasProperties:
            try:
                if prop.is_a("IfcPropertySingleValue"):
                    value = prop.NominalValue.wrappedValue
                elif prop.is_a("IfcPropertyEnumeratedValue"):
                    value = ','.join([val.wrappedValue for val in prop.EnumerationValues.Values])
                elif prop.is_a("IfcPropertyBoundedValue"):
                    value = f"{prop.BaseValue.lower} - {prop.BaseValue.upper}"
                else:
                    value = 'N/A'
                params[prop.Name] = value
            except Exception as e:
                print(f"Errore nell'estrazione del parametro {prop.Name} per l'elemento {element.GlobalId}: {e}")
                params[prop.Name] = 'N/A'
    return params

def collect_all_parameters(elements):
    """
    Raccoglie tutti i nomi dei parametri unici presenti negli elementi.
    
    :param elements: Lista di elementi IFC
    :return: Set di nomi dei parametri
    """
    param_set = set()
    for element in elements:
        property_sets = get_property_sets(element)
        for pset in property_sets:
            for prop in pset.HasProperties:
                if hasattr(prop, 'Name'):
                    param_set.add(prop.Name)
    return param_set

def convert_ifc_to_csv_complete(ifc_file_path, csv_file_path):
    """
    Converte un file IFC in un file CSV includendo tutte le informazioni degli elementi.
    
    :param ifc_file_path: Percorso al file IFC
    :param csv_file_path: Percorso dove salvare il file CSV
    """
    try:
        # Carica il file IFC
        ifc_model = ifcopenshell.open(ifc_file_path)
    except Exception as e:
        print(f'Errore nell\'apertura del file IFC: {e}')
        return
    
    # Recupera gli elementi 'IfcProduct' e 'IfcProxy'
    product_elements = ifc_model.by_type('IfcProduct')
    proxy_elements = ifc_model.by_type('IfcProxy')
    all_elements = product_elements + proxy_elements

    # Raccogli tutti i nomi dei parametri unici
    all_parameters = collect_all_parameters(all_elements)
    
    # Definisci le intestazioni del CSV
    headers = ['GUID', 'Name', 'Type', 'Description', 'X', 'Y', 'Z'] + sorted(all_parameters)
    
    try:
        # Apri il file CSV per scrittura
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            
            # Scrivi l'intestazione del CSV
            csv_writer.writeheader()
            
            # Itera attraverso tutti gli elementi
            for element in all_elements:
                row = {
                    'GUID': element.GlobalId,
                    'Name': element.Name if element.Name else 'N/A',
                    'Type': element.is_a(),
                    'Description': element.Description if hasattr(element, 'Description') else '',
                }
                
                # Ottieni la posizione dell'elemento
                x, y, z = get_element_location(element)
                row['X'] = x
                row['Y'] = y
                row['Z'] = z
                
                # Estrai tutti i parametri dell'elemento
                params = get_element_parameters(element)
                for param in all_parameters:
                    row[param] = params.get(param, 'N/A')
                
                # Scrivi la riga nel CSV
                csv_writer.writerow(row)
                    
    except Exception as e:
        print(f'Errore nella scrittura del file CSV: {e}')
        return
    
    print(f'Conversione completata! File CSV salvato come {csv_file_path}')

# Percorsi ai file IFC e CSV
ifc_file_path = 'C:/Users/arman/Desktop/Microservizi/Ifc_to_CSV/file.ifc'
csv_file_path = 'C:/Users/arman/Desktop/Microservizi/Ifc_to_CSV/output_complete.csv'

# Chiama la funzione di conversione
convert_ifc_to_csv_complete(ifc_file_path, csv_file_path)