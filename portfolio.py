from pathlib import Path
from PIL import Image
import json
import streamlit as st
from streamlit_lottie import st_lottie


THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Animation - 1711444537094.json"

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")

# Display lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Apply CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Loading assets

img_homepage = Image.open("images/homepage.png")
img_sync_folders = Image.open("images/syncfolders.png")
img_counting_slides = Image.open("images/count_slides.png")
img_microwave_oven = Image.open("images/microwave_oven.png")
img_bdd_testing_jules = Image.open("images/jules.png")
img_bdd_testing_emag = Image.open("images/emag.png")
img_carturesti = Image.open("images/carturesti.png")

# header section

with st.container():
    st.subheader("Hi, I am Cristina:wave:")
    st.title("A Junior Python Developer from Bucharest")
    st.write(
             "I have a strong enthusiasm for delving into Python, constantly\n"
             "seeking fresh approaches to utilize it effectively and efficiently in everyday tasks."
            )

# what I do

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Continuously striving for self-improvement, 
            I thrive within collaborative team environments, constantly seeking to enhance my skills. 
            - I write Python scripts to scrape website data.
            - I invest my free time in updating my GitHub account with new projects.
            - I am persistently working to enhance my expertise in Python.\n
            Coding it's a way of life, a boundless journey of exploration and creation that fuels my every thought and action.\n
            My passion for coding goes beyond the mere act of problem-solving.
            It's about the journey of self-discovery and growth that coding facilitates. 
            """
        )


    with right_column:
        lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
        st_lottie(lottie_animation, key="coding", height=400)

# My Projects

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column=st.columns((1,2))

    with image_column:
        st.image(img_homepage)


    with text_column:
        st.subheader("Ecommerce app")
        st.write(
            """
            - This is a website for an online gift shop, allowing users to browse a catalog of available presents and make purchases electronically.
            - Users can seamlessly process orders, submit them for fulfillment, and complete payments online. 
            - The web application was developed utilizing the Python programming language and the Django Web Framework.
            """
        )

        st.markdown("[See github...] (https://github.com/canghelet/Examen_ANC-Magazin_online_de_cadouri.git)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_sync_folders)
    with text_column:
        st.subheader("Sync folders script project")
        st.write(
            """
              This is my sync folders script written in Python.
            - The script aims to synchronize two folders: the source and the replica.
            - It will ensure that the replica folder maintains a complete and identical copy of the source folder.
            - This synchronization process is one-way, meaning that after synchronization, the content of the replica 
            folder will be adjusted to precisely match the content of the source folder.
            - Synchronization will occur periodically.
            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/Sync_folders_script.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_counting_slides)
    with text_column:
        st.subheader("PPT slide count script")
        st.write(
            """

            - Python script developed to count the number of decks in PowerPoint presentations.
            -  As input, the script will take one or more PowerPoint files and generates a report showing the number of slides for each deck,
            along with the name of the deck. 
            - Additionally, it provides a summary that shows the total number of slides across all processed presentations.
            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/PPT_slide_count_script.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_microwave_oven)
    with text_column:
        st.subheader("Microwave Oven")
        st.write(
            """

            - Project, titled "Microwave Oven," was developed in the C programming language.
            - Utilizes PIC16F877A microcontroller, with the aim of emulating the typical functions of a microwave oven.
            - Utilizing PICSimLab, the behavior of an embedded controller within a microwave oven is replicated.\n
            Feel free to explore how the project works and how microwave oven can be simulated by watching the below link:
            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/Microwave_Oven.git)")
        st.markdown("[Watch video...] (https://www.youtube.com/watch?v=z7zAjMgdGnA)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_bdd_testing_jules)
    with text_column:
        st.subheader("BDD Testing project")
        st.write(
            """

            Jules BDD Automation Framework project written in Python.

            - Site tested: https://jules.app/     
            - Design pattern used: page object model   
            - Methodology: behavior driven development
                
            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/Jules_BDD_Testing.git)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_bdd_testing_emag)
    with text_column:
        st.subheader("BDD Testing project")
        st.write(
            """

            Emag BDD Automation Framework project written in Python.

            - Site tested: https://www.emag.ro/  
            - Design pattern used: page object model  
            - Methodology: behavior driven development
            
            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/Emag_BDD_Testing.git)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_carturesti)
    with text_column:
        st.subheader("Selenium Script")
        st.write(
            """

            Web automation script, developed using Python and Selenium, having as purpose, automation of various browser tasks on the "https://carturesti.ro/" website: 
            - Navigate to the "https://carturesti.ro/" webpage, maximize the window, and retrieve all the links on the webpage.
            - Perform a search using the term "carti" and display the search results, showcasing each book and adding them to the cart.
            - Navigate through pages by accessing each button from the navigation bar, populate and submit a web form to subscribe to the website newsletter.

            """
        )
        st.markdown("[See github...] (https://github.com/canghelet/python_selenium_script.git)")

# contact form

with st.container():
    st.write("---")
    st.header(" Get In Touch With Me! ")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/cristina.anghelet@gmail.com" method="POST">
    <input type ="hidden" name ="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder ="Your e-mail" required>
     <textarea name ="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()










