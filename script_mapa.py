
import pandas as pd
import folium 


M_moricandioides =pd.read_csv('Moricandia_moricandioides2.csv', sep='\t')
M_foetida =pd.read_csv('M_foetida2.csv', sep='\t')
M_rytidocarpoides =pd.read_csv('M_rytidocarpoides1.csv', sep=';')

logoIcon= folium.features.CustomIcon('Moricandia_rytidocarpoides.jpg', icon_size=(50,50))

frames= [M_moricandioides, M_foetida, M_rytidocarpoides]
moricandias= pd.concat(frames)
moricandias=moricandias.dropna(subset=['decimalLongitude'])

moricandias=moricandias.dropna(subset=['decimalLatitude'])

moricandioides= folium.Map(
        location=[38,-4],
        tiles='Stamen Terrain',
        zoom_start=8
)
for indice, ocurrencia in moricandias.iterrows():
    longitude =ocurrencia['decimalLongitude']
    latitude =ocurrencia['decimalLatitude']
    
    if not pd.isnull(latitude): 
        marca_moricandioides= folium.Marker(location=[latitude,longitude],
                                            popup=' Moricanda moricandioides',
                                            icon=folium.Icon(icon='leaf',color='green'))
        marca_rytidocarpoides=folium.Marker(location=[latitude,longitude],
                                            popup='Moricandia rytidocarpoides',
                                            icon=folium.Icon(icon='leaf',color='yellow'))
        marca_foetida= folium.Marker(location=[latitude,longitude],
                                     popup='Moricandia foetida',
                                     icon=folium.Icon(icon='leaf',color='purple'))
        
        if ocurrencia['species'] == 'Moricandia moricandioides':
            marca_moricandioides.add_to(moricandioides)
        elif ocurrencia ['species'] == 'Moricandia foetida':
            marca_foetida.add_to(moricandioides)
        elif ocurrencia ['species'] == 'Moricandia rytidocarpoides':
            marca_rytidocarpoides.add_to(moricandioides)

moricandioides.save('Moricandia_andalucia.html')

