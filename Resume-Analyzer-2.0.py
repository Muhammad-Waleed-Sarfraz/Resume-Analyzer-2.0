import PyPDF2 # To call a library which read pdf data
from google import genai # To call google ai agent
# Actual Function 
def extract_text(filename):
    reader = PyPDF2.PdfReader(filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

client = genai.Client(api_key ="Your_API_Key ")
#To job description 
print("Choose an option to upload your JD \n1. Upload Text\n2. Upload Pdf")
choice = input("What You Want to do : ")
if (choice == "1"):
    JD_Data = input("Upload your text here :").lower()
    # print(JD_text)
elif (choice == "2"):
    JD_Data = extract_text("JD.pdf")
    # print("JD_Data")
else:
    print("----Invalid Choice----")
# To Upload Resume
print("Choose an option to upload your resume data \n1. Upload Text\n2. Upload Pdf")
choice = input("What You Want to do : ").lower()
if (choice == "1"):
    Resume_Data = input("Upload Your data here : ")
    # print(Resume_text)
elif (choice == "2"):
    Resume_Data = extract_text("resume.pdf")
    # print(Resume_Data)
else:
    print("----Invalid Choice----")

ai_prompt = print(f"Act as an professional recruiter and read the job description :{JD_Data}. And the the resume: {Resume_Data}.Calculate " \
"the match score and also create a different list for matching and missing skills.")
print("Loading AI Analysis Report (This may take a few secons)......")
response = client.model.generate_content(model='gemini-3.8-flash', contents=ai_prompt)
print("----AI Analysis Report----")
print(response.text)
