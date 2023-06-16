import streamlit as st
st.title("Salary Estimate Calculator")


st.sidebar.write('KEYWORDS:')

st.sidebar.write('Sal = Salary')
st.sidebar.write('Minwage = Minimum wage')
st.sidebar.write('YearsofExp = Years of experience')
st.sidebar.write('Skillprof = Skill proficiency')

st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")

st.sidebar.write('PLEASE NOTE:')

st.sidebar.write('For Years of Experience < 3,')
st.sidebar.write('Sal = Minwage x YearsofExp x Skillprof')

st.sidebar.text(" ")

st.sidebar.write('For Years of Experience > 3,')
st.sidebar.write('Sal = (Minwage x 1.5) x YearsofExp x Skillprof')

st.sidebar.text(" ")

st.sidebar.write('For Years of Experience > 15,')
st.sidebar.write('Sal = (Minwage x 2) x YearsofExp x Skillprof')

st.sidebar.text(" ")
st.sidebar.text(" ")

st.sidebar.write('SKILL PROFICIENCY LEVELS:')
st.sidebar.write ('1 = Beginner')
st.sidebar.write ('2 = Advanced beginner')
st.sidebar.write ('3 = Competent/Intermediate')
st.sidebar.write ('4 = Proficient/Advanced Intermediate')
st.sidebar.write ('5 = Expert')

st.sidebar.text(" ")
st.sidebar.text(" ")

st.sidebar.write('*The employer reserves the right to assess the skill proficiency level of the employee during/after the interview process and review the salary expectation accordingly.')

st.sidebar.text(" ")
st.sidebar.text(" ") 

st.sidebar.write('*For SOME countries, the National Job Board reserves the right to approve or disapprove the information provided here if found to be false. If your is verified, you will be issued a certificate which ascertains your skill and experience level and the commesurate salary attached. This certificate can be presented to prospective or current employers to negotiate your salary.')

st.text(" ")
st.text(" ")

st.write("I created this application to help job seekers, employees, and HR professionals/employers calculate the salary expectation for a role based on the candidate's skills and work experience. The estimated salary is calculated using the country's minimum wage, the skills of the job seeker, and relevant work experience. The app is seamless and easy to use.")
st.write("If you're viewing this with a mobile phone, please open the sidebar at the top left corner for necessary information.")
st.write('🥂 To bigger salaries!')



st.text(" ")
st.text(" ")

col1, col2 = st.columns(2, gap="large")

with col1:
    
    st.write("NOW LET'S CALCULATE...")
    
    st.selectbox("Course of study", ["Accounting", "Banking and Finance", "Business Administration", "Communications", "Computer Science", "Economics", "Law", "Medicine", "Political Science", "Zoology", "Others"])

    st.selectbox("Current/Preferred Industry", ["Advertising", "Agriculture", "Arts", "Aviation", "Banking", "Consultancy", "Education", "E-commerce", "Energy", "Entertainment", "Fashion", "Health", "Hospitality and Tourism", "Information and Technology", "Law", "Manufacturing", "NGO", "Public Sector", "Startup", "Telecommunications", "Others"])

    st.selectbox("Area of Interest", ["Administration", "Accounting/Audit", "Banking/Finance", "Customer Service", "Cyber security", "Data/Business Analytics", "Human Resources", "Legal", "Operations", "Marketing/Sales", "Product", "Software Development", "Supply Chain", "Startup", "UI/UX Designer", "Others"])

    st.selectbox("Major Skill", ["Business Analysis", "Business Development", "Communication", "Database Administration", "Data Analytics", "Data Engineering", "Data Science/Machine Learning", "Deep Learning", "Digital Marketing", "Economics", "Law",  "Writing", "Web Development", "Product Management", "Project Management", "Relationship Management", "Social Media Management", "Design", "Others"])
    
    st.text_input("Major Software/Language")


with col2:
    
    st.text(" ")
    st.text(" ")
    st.text(" ")
    
    st.radio("Age range", ["18-25", "26-35", "36-45", "46-65"])
    
    st.text(" ")

    st.radio("Identification Type", ["National Identity Card", "International Passport", "Driver's Licence", "Worker's/Resident Permit", "Voter's Card"])
    
    st.number_input("ID Number", step = 1)

st.text(" ")
st.text(" ")
    
Minwage = st.number_input("What is your country's minimum wage", step = 1)
YearsofExp = st.number_input("How many years of work experience do you have", step = 1)
Skillprof = st.radio("What is your skill proficiency level", [1,2,3,4,5])

st.text(" ")    

st.checkbox("Would you like us to match you with an employer?")
    
st.text(" ")
st.text(" ")    

if st.button("Calculate Salary"):
    Sal = Minwage*YearsofExp*Skillprof
   
    st.write(f'Your Salary Expectation is  {Sal}. \n We will verify your information and send you an approval or unverified email within 5 to 10 working days. \n If the information provided is correct, your verification certificate will be uploaded on the National Job Board. \n All the best!')
            
             
