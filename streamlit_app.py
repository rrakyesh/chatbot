import streamlit as st
from document_parser import parse_document
from rule_engine import evaluate_document
from model_integration import run_llm

# Streamlit app title
st.title("Document Rule Evaluation App")

# Upload document
uploaded_file = st.file_uploader("Upload a document (PDF or DOCX)", type=["pdf", "docx"])

# Display input field for rule entry
rules = st.text_area("Enter rules (one rule per line)", height=200)

if uploaded_file and rules:
    # Parse the document
    document_content = uploaded_file.read()
    parsed_text = parse_document(document_content)
    
    # Split rules into a list
    rule_list = rules.splitlines()

    # Display the parsed document
    st.subheader("Parsed Document:")
    st.write(parsed_text)

    # Perform rule evaluation
    if st.button("Evaluate Document"):
        result = evaluate_document(parsed_text, rule_list)
        st.subheader("Evaluation Results:")
        st.write(result)

        # (Optional) Call LLM for advanced analysis (if needed)
        if st.checkbox("Run LLM for advanced analysis"):
            llm_results = run_llm(parsed_text, rules)
            st.subheader("LLM Results:")
            st.write(llm_results)
