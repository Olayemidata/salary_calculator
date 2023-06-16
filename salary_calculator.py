import streamlit as st
st.title("Salary Estimate Calculator")


st.sidebar.write('PLEASE NOTE:')

st.sidebar.write('For Years of Experience < 7,')
st.sidebar.write('Sal = Minwage * YearsofExp * Skillprof')

st.sidebar.text(" ")

st.sidebar.write('For Years of Experience > 7,')
st.sidebar.write('Sal = (Minwage*1.5) * YearsofExp * Skillprof')

st.sidebar.text(" ")

st.sidebar.write('For Years of Experience > 15,')
st.sidebar.write('Sal = (Minwage*2) * YearsofExp * Skillprof')


st.sidebar.text(" ")
st.sidebar.text(" ")

st.sidebar.write('KEYWORDS:')

st.sidebar.write('Sal means Salary')
st.sidebar.write('Minwage means Minimum wage')
st.sidebar.write('YearsofExp means Years of experience')
st.sidebar.write('Skillprof means Skill proficiency')


st.sidebar.text(" ")
st.sidebar.text(" ")

st.sidebar.write('*This App is used to calculate the salary expectation for a role.')

st.sidebar.text(" ")
st.sidebar.text(" ") 

st.sidebar.write('*For SOME countries, the National Job Board reserves the right to approve or disapprove the information provided here if found to be false. If your is verified, you will be issued a certificate which ascertains your skill and experience level and the commesurate salary attached. This certificate can be presented to prospective or current employers to negotiate your salary.')



st.text(" ")
st.text(" ")

col1, col2 = st.columns(2, gap="large")

with col1:

    st.selectbox("Course of study", ["Accounting", "Banking and Finance", "Business Administration", "Communications", "Computer Science", "Economics", "Law", "Medicine", "Political Science", "Zoology", "Others"])

    st.selectbox("Current/Preferred Industry", ["Advertising", "Agriculture", "Arts", "Aviation", "Banking", "Consultancy", "Education", "E-commerce", "Energy", "Entertainment", "Fashion", "Health", "Hospitality and Tourism", "Information and Technology", "Law", "Manufacturing", "NGO", "Public Sector", "Startup", "Telecommunications", "Others"])

    st.selectbox("Area of Interest", ["Administration", "Accounting/Audit", "Banking/Finance", "Customer Service", "Cyber security", "Data/Business Analytics", "Human Resources", "Legal", "Operations", "Marketing/Sales", "Product", "Software Development", "Supply Chain", "Startup", "UI/UX Designer", "Others"])

    st.selectbox("Major Skill/Software", ["Business Analysis", "Business Development", "Communication", "CRM/Saleforce",  "Database Administration", "Data Analytics", "Data Engineering", "Data Science/Machine Learning", "Deep Learning", "Digital Marketing", "Economics", "Law",  "Writing", "Web Development", "Product Management", "Project Management", "Relationship Management", "Social Media Management", "Design", "Others"])


with col2:
    
    st.radio("What is your age range", ["18-25", "26-35", "36-45", "46-65"])

    st.radio("Identification Type", ["National Identity Card", "International Passport", "Driver's Licence", "Worker's/Resident Permit", "Voter's Card"])

    st.number_input("Please enter your ID Number", step = 1)

st.text(" ")
st.text(" ")
st.text(" ")
    
    
Minwage = st.number_input("What is your country's minimum wage", step = 1)
YearsofExp = st.number_input("How many years of work experience do you have", step = 1)
Skillprof = st.radio("What is your skill proficiency level", [0,1,2,3,4,5])

st.text(" ")
st.text(" ")  

st.write("***Please open sidebar at the top left corner if you're using a mobile phone for important information")

st.text(" ")  

st.checkbox("Would you like us to match you with an employer?")

    
st.text(" ")
st.text(" ")    
    

if st.button("Calculate Salary"):
    Sal = Minwage*YearsofExp*Skillprof
   
    st.write(f'Your Salary Expectation is  {Sal}. \n We will verify your information and send you an approval or unverified email within 5 to 10 working days. \n If the information provided is correct, your verification certificate will be uploaded on the National Job Board. \n All the best!')
            
             
