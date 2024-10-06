#run the script local with:
#py -m streamlit run habitable_worlds_observatory_navigator.py
#app will open in a new tab in default web browser

import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None 
import matplotlib.pyplot as plt
import streamlit as st

st.header("Navigator for the Habitable Worlds Observatory(HWO):telescope:")

def load_data():
    df = pd.read_csv("data/PSCompPars_2024.10.05_02.57.49.csv")
    #df = pd.read_csv("PSCompPars_2024.10.05_02.57.49.csv")
    df = df[['pl_name','hostname', 'discoverymethod', 'disc_year', 'pl_rade', 'st_rad', 'pl_orbsmax', 'sy_dist']]
    return df

def calculate_limiting_distance(d, ps):
    return 15 * (d / 6) / ps

#SNR0 [(R* RP (D/6)) / ((ES/10) PS)]2
def calculate_snr(rs, rp, d, es, ps):
    return ((rs*rp*(d/6))/((es/10)*ps))*2

def expand_data(df, d):
    df['es_max'] = calculate_limiting_distance(d, df.pl_orbsmax)
    df['snr'] = calculate_snr(df.st_rad, df.pl_rade, d, df.sy_dist, df.pl_orbsmax)
    df['disc_year'] = df['disc_year'].astype('str')
    df.rename(columns={'pl_name':'planet name','hostname':'stellar name', 'disc_year':'discovery year', 'pl_rade':'planetary radius(earth radius)', 'st_rad':'stellar radius(solar radius)', 'pl_orbsmax':'planet-star distance(AU)', 'sy_dist':'distance to the planetary system(pc)'}, inplace=True)
    #df.set_index('planet name', inplace=True)
    return df

df = load_data()
total_num = len(df.index)
st.set_option("client.showErrorDetails", False)

tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Exoplanetes", "Navigator", "Mapper"])

with tab1:
    st.header('2024 NASA Space Apps Challenge')
    st.subheader('Mapping the Characterizable Exoplanets in our Galaxy')
    st.text('Since 1995, thousands of planets orbiting stars other than our Sun (exoplanets)')
    st.text('have been discovered. Most of these exoplanets are gas giants that orbit very ')
    st.text('close to their stars. Exoplanets have been discovered mainly using indirect ')
    st.text('methods, e.g., by measuring the effect that they have on their host stars.')
    st.text('Since an exoplanet’s signal is so small compared to that of its star, it has ')
    st.text('been extremely difficult to identify exoplanets directly. HWO is an upcoming ')
    st.text('Great Observatory concept that NASA is developing to directly image exoplanets ')
    st.text('and expand our knowledge of these Earth-like bodies.')
    st.text('When planning for this next-generation mission, it is helpful to ')
    st.text('understand how the instrument parameters can impact the physical ')
    st.text('parameters that we can explore.')
    st.link_button("Get more information about HWO", "https://science.nasa.gov/astrophysics/programs/habitable-worlds-observatory/")
    st.link_button("More about NASA Sapce Apps Challenge", "https://www.spaceappschallenge.org/nasa-space-apps-2024/challenges/navigator-for-the-habitable-worlds-observatory-hwo-mapping-the-characterizable-exoplanets-in-our-galaxy/?tab=details")
    st.image('https://science.nasa.gov/wp-content/uploads/2024/05/gl12b-illustration-less-atmosphere-ac.jpg?anchor=center&mode=crop&width=730&height=410', caption="Gliese 12 b, which orbits a cool red dwarf star located just 40 light-years away. Artist’s concept. NASA/JPL-Caltech/R. Hurt (Caltech-IPAC)")
    st.caption('Credits: NASA https://www.spaceappschallenge.org/contact-us/')
    
with tab2:
    st.header('What is an exoplanet?')
    st.text('An exoplanet is a planet that is outside our solar system.') 
    st.text('Exoplanets are typically found orbiting a star other than our Sun. In the same ')
    st.text('way that our solar system contains eight planets, other stars can have many ')
    st.text('exoplanets in orbit around them.')
    st.image('https://www.asc-csa.gc.ca/images/astronomie/au-dela-systeme-solaire/exoplanetes-id-17211-ban.jpg?anchor=center&mode=crop&width=730&height=410', caption="An artist's concept of several stars orbited by exoplanets.(Credit: ESO/M. Kornmesser)")
    st.header('Types of exoplanets')
    st.text('A wide variety of planets exist in our solar system, ranging from rocky planets ')
    st.text('(like Earth) to gas giants (like Jupiter). Exoplanets are even more diverse. ')
    st.text('Here are some of the types of exoplanets:')
    st.subheader('Hot Jupiters:ringed_planet:')
    st.text('Large gas giants like Jupiter, but with one key difference – they ')
    st.text('are found very close to their host star, even closer than Mercury')
    st.text('is to the Sun')  
    st.subheader('Mini-Neptunes and Super-Earths:earth_africa: ')
    st.text('The most common type of exoplanet observed by ')
    st.text('scientists, these could be supersized rocky planets, ')
    st.text('or gas planets smaller than Neptune')
    st.text('According to astronomers, over 50 percent of stars likely host at least one planet.')
    st.text('Scientists continue to discover surprising alien worlds.')
    st.link_button("More about Famous exoplanets like 51 Pegasi b :alien:", "https://www.asc-csa.gc.ca/eng/astronomy/beyond-our-solar-system/exoplanet-zoo.asp")
    
    st.header('How do astronomers discover new exoplanets?')
    st.subheader('Transit method:sunny::new_moon:')
    st.text('For an observer, when a planet passes in front of its star, it is called')
    st.text(' a "transit." When this happens, the brightness of the star appears to decrease')
    st.text('temporarily. Astronomers can detect exoplanets by spotting these dips in the ')
    st.text('brightness of stars. Certain space missions like NASA\'s Kepler Space Telescope ')
    st.text('have been designed to  detect these temporary changes. Based on the frequency ')
    st.text('of these light variations, scientists can determine the size and orbital period ')
    st.text('of the exoplanets.')
    st.text('Three-quarters of known exoplanets have been discovered using the transit method!')
    st.subheader('Radial velocity method:ambulance::rainbow:')
    st.text('A planet travels along its orbit because of the gravitational pull of its star.')
    st.text('But did you know that stars also move slightly – or wobble – because of ')
    st.text('the gravitational effect of their planets?')
    st.text('The first exoplanet ever detected around a Sun-like star, 51 Pegasi b, ')
    st.text('was discovered using the radial velocity method in 1995.')
    st.text('Here\'s how it works: as a star wobbles, the light it emits is affected.')
    st.text('Scientists can calculate how fast a star is wobbling by measuring the ')
    st.text('intensity of the Doppler effect – the stretching and compression of lightwaves.')
    st.text('The faster the wobble, the bigger and closer the planet orbiting the star!')
    st.link_button("More about Detecting exoplanets", "https://www.asc-csa.gc.ca/eng/astronomy/beyond-our-solar-system/detecting-exoplanets.asp")
    st.caption('Credits: Canadian Space Agency https://www.asc-csa.gc.ca/eng/about/')
    st.subheader('Distribution of Discovery methods')
    st.text('Based on NASA Exoplanet Archive data.')
    st.image('data/discoverymethods.png')
    
with tab3:
    st.header('Most promising candidates for HWO to observe')
    st.text('The ability of HWO to detect and characterize exoplanets depends on ')
    st.text('the stellar-radius (R* [Rsun]), the planetary radius (RP [REarth]), ')
    st.text('the planet-star distance (PS [AU]), the distance to the planetary ')
    st.text('system (ES [pc]), and the diameter of the telescope (D [m]).')
    st.divider()
    st.text(' Two key parameters will define the ability of HWO to characterize an exoplanet:')
    st.subheader('1. the distance to the exoplanetary system')
    st.text('— the further the distance to the exoplanet, the fainter')
    st.text('and closer to its host star it appears.')
    st.subheader('2. the diameter of the HWO telescope')
    st.text('— a bigger telescope allows us to better separate the exoplanet from the star.')
    st.subheader('', divider='orange')
    diameter = st.slider("How big is the telescope diameter?", 5, 15, 6)
    st.write("The telescope diameter is ", diameter, " m")

    df_ex = expand_data(df.copy(), diameter)
    filt = (df_ex['distance to the planetary system(pc)'] <= df_ex.es_max) & (df_ex.snr > 5)
    candidates = df_ex.loc[filt]
    num_candidates = len(candidates.index)
    percentage = round((num_candidates/total_num*100), 2)
    
    st.write('Total number of exoplanets: ', total_num)
    st.write('Number of promising candidates: ', num_candidates)
    st.write('Percentage of promising candidates: ', percentage, ' %')
    
    #st.dataframe(candidates)
    candidates = pd.DataFrame(candidates)
    event = st.dataframe(
        candidates,
        on_select="rerun",
        selection_mode="single-row",
    )
    
    st.text('The data is filtered by the signal-to-noise ratio (SNR) greater than 5')  
    st.text('and that the planet and star can be separated accurately (ESmax).')

    st.caption('Data credits')
    st.caption('NASA Exoplanet Archive - This file was produced by')
    st.caption('http://exoplanetarchive.ipac.caltech.edu on Sat Oct 5 2024')
    st.caption('Further credits')
    st.caption('The Astronomical Journal - Probing the Capability of Future')           
    st.caption('Direct-imaging Missions to Spectrally Constrain the Frequency of ')
    st.caption('Earth-like Planets Jade H. Checlair et al 2021')

with tab4:
    planet = event.selection.rows
    planet_df = candidates.iloc[planet]
    #st.dataframe(planet_df)
    if len(planet_df) > 0:
        name = planet_df.iloc[0, 0]
        st.subheader('You have chosen')
        st.header(name)
        year = planet_df.iloc[0, 3]
        method = planet_df.iloc[0, 2]
        radius = planet_df.iloc[0, 4]
        distance = planet_df.iloc[0, 6]
        pc = planet_df.iloc[0, 7]
        st.write('The planet was discovered ', year, ' by ', method, '.')
        st.write('It\'s planetary radius is ', radius, ' (earth radius)')
        st.write('and it orbits its star in ', distance, ' AU distance.')
        st.write('The planetary system is ', pc, ' pc away.')
        st.subheader('Starmap')
        st.text('tbd')
        st.image('https://starplot.dev/images/examples/star_chart_detail.png?anchor=center&mode=crop&width=730&height=410', caption="Example map from starplot https://starplot.dev/")
        st.divider()
        st.caption('earth radius = 6,357 km (3,950 mi)')
        st.caption('AU (Astronomical unit) = average earth-sun distance')
        st.caption('pc (Parsec) = 3.26 light-years or 206,265 AU')
    else:
        st.subheader("No planet selected.")
        st.image('https://www.asc-csa.gc.ca/images/recherche/tiles/2240058a-e9ce-43e8-baac-0a3a0acb531e.jpg?anchor=center&mode=crop&width=730&height=410', caption="An artist's concept of Proxima Centauri b, the closest exoplanet to our solar system. (Credit: ESO)")
    
    
