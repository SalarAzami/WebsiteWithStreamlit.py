from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 
#pass
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# --- Simple gate (password) ---
PASSWORD = st.secrets.get("APP_PASSWORD") or os.environ.get("APP_PASSWORD")
pw = st.text_input("Enter password:", type="password")
if pw != PASSWORD:
    st.stop()
    
# page config
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()      
    
    
#  Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#  ----- HEADER SECTION  -----

with st.container():
    st.subheader("Hello, I'm MOSA👋🏽 ")
    st.title("A Data & Process Analyst From IRAN ")
    st.write("I am passionate about finding ways to use 'PYTHON' and VBA to be more efficient")
    st.write("[Learn More >](www.linkedin.com/in/mo-salar-azami-579075128)")




#   ----LOAD ASSETS -----
lottie_coding = load_lottieurl("https://lottie.host/8ca41b88-90ca-4b4f-be25-7f5329eb6d77/AHQuvR8ESg.json")
imag_path = "images/Designer.jpeg"
img_contact_form = Image.open(imag_path)
st.image(img_contact_form)




#  ----  WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
    """
I don't need to go on a Vacation as long as i have "PYTHON" , "DATA". with PyDa always on trip not the world,it's not enough; but whole UNIVERSE😉!
\n
    .Recognized career misalignment: Acknowledge the mismatch between skills and career path.
    .Embraced passion for Python and Data: Engage in learning and mastering 
    Python programming language and data-related skills.
    
    .Pursued retraining or upskilling: Enroll in courses or training programs
    to develop expertise in Python and data analysis.
    
    .Explored career transition opportunities: Investigate roles in data science, analytics,
    or software development aligned with newfound passion.
    
    .Networked and sought mentorship: Connect with professionals in the Python and data community
    for guidance and advice on career transition steps.

    """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
        

# ----- PROJECTS -----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    
    image_column, text_column = st.columns((1, 2))
    imag_path = "images/yek.jpeg"

    
    with image_column:
        img_contact_form = Image.open(imag_path)
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("Integrate animations like 'Lottie Animations' inside yourn Streamlit App")
        st.write(
    """
    Learn how to use Lottie Files in Streamlit!
    Animations make our Web app more engaging and fun, and Lottie Files are the easiest way to do it.
    in this tutorial, You'll see exactly how to do it.
    """
        )
        st.markdown("[Watch Video...](https://youtu.be//TXSOitGoINE)")
        


# ---- CONTACT -----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me:")
    st.write("##")
    
    #Documentation: https://formsubmit.co/
    contact_form= """
    <form action="https://formsubmit.co/Azami11169@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your Name" required>
        <input type="email" name="email" Placeholder="Your E-Mail" required>
        <textarea name="Message" Placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
