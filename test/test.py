import streamlit as st

def main():
    st.title("My Portfolio Dashboard")

    # Introduction
    st.header("Introduction")
    st.write("""
    Hello! I'm [Your Name], a passionate developer/data scientist with experience in [Your Skills].
    This is a brief overview of my projects and experiences.
    """)

    # Projects
    st.header("Projects")
    projects = {
        "Project 1": {
            "description": "This project is about ...",
            "link": "https://github.com/yourusername/project1"
        },
        "Project 2": {
            "description": "This project focuses on ...",
            "link": "https://github.com/yourusername/project2"
        },
        # Add more projects as needed
    }

    for project_name, project_info in projects.items():
        st.subheader(project_name)
        st.write(project_info["description"])
        st.write(f"[Link to the project]({project_info['link']})")

    # Contact
    st.header("Contact")
    st.write("""
    Feel free to reach out to me!
    - Email: [youremail@example.com](mailto:youremail@example.com)
    - LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourusername/)
    - GitHub: [Your GitHub Profile](https://github.com/yourusername)
    """)

if __name__ == "__main__":
    main()
