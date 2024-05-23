import streamlit as st
import pandas as pd
import os

# folder_path = os.getcwd()
# file_name = "df_final.csv"
# full_path = os.path.join(folder_path, file_name)

# data = pd.read_csv(full_path)
# df = pd.DataFrame(data)


def IntroPage():

    def intro():
        import streamlit as st

        st.write("## Explore Health Statistics with Andrzej and Marta! 👋")

        st.sidebar.success("Select what you want to see above.")

        st.markdown(
            """

            **👈 Select a demo from the dropdown on the left** to see some examples
            of what we've done!

            ### Want to learn more abour Streamlit?

            - Check out [streamlit.io](https://streamlit.io)
            - Jump into our [documentation](https://docs.streamlit.io)
            - Ask a question in our [community
            forums](https://discuss.streamlit.io)

            ### See more complex demos

            - Use a neural net to [analyze the Udacity Self-driving Car Image
            Dataset](https://github.com/streamlit/demo-self-driving)
            - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
        """
        )

    def Plotting_Page():
        import streamlit as st
        import pandas as pd
        import os
        from create_graph import Scatter

        st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
        st.write(
            """
            This demo illustrates our scatter plot!
            """
        )
        folder_path = os.getcwd()
        file_name = "df_final.csv"
        full_path = os.path.join(folder_path, file_name)

        data = pd.read_csv(full_path)
        df = pd.DataFrame(data)

        Scatter(df)

        # progress_bar = st.sidebar.progress(0)
        # status_text = st.sidebar.empty()

        # progress_bar.empty()

        # # Streamlit widgets automatically run the script from top to bottom. Since
        # # this button is not connected to any other logic, it just causes a plain
        # # rerun.
        # st.button("Re-run")

    def mapping_demo():
        import streamlit as st
        from create_map import Map

        st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
        st.write(
            """
            This demo illustrates our MAP plot!
            """
        )
        folder_path = os.getcwd()
        file_name = "df_final.csv"
        full_path = os.path.join(folder_path, file_name)

        data = pd.read_csv(full_path)
        df = pd.DataFrame(data)
        Map()

    def Pictogram():
        from create_pictogram import CreatePictogramChart
        import streamlit as st
        import matplotlib.pyplot as plt
        from pywaffle import Waffle
        import pandas as pd

        st.markdown(f'# {list(page_names_to_funcs.keys())[3]}')
        st.write(
            """
            This demo illustrates our Pictograms done by Andrew!
            """
        )
        CreatePictogramChart()


    # def Other_Graphs():
    #     import streamlit as st
    #     import matplotlib.pyplot as plt
    #     import numpy as np
    
    
    #     st.markdown(f'# {list(page_names_to_funcs.keys())[4]}')
    #     st.write(
    #         """
    #         This demo illustrates a random simple graph!
    #         """
    #     )
    
    #     # Generate random data
    #     x = np.random.rand(10)
    #     y = np.random.rand(10)
    
    #     fig, ax = plt.subplots()
    #     ax.scatter(x, y)
    
    #     st.pyplot(fig)

    def Other_Graphs():
        import streamlit as st
        import pandas as pd
        import os
        from create_suicide_graph import CreateSuicideGraph

        st.markdown(f'# {list(page_names_to_funcs.keys())[4]}')
        st.write(
            """
            This demo illustrates a random simple graph!
            """
        )

        CreateSuicideGraph()

    # add function here to display rest of the graphs in a separate tab!

    page_names_to_funcs = {
        "—": intro,
        "Plotting Demo": Plotting_Page,
        "Mapping Demo": mapping_demo,
        "Pictogram Demo": Pictogram,
        "Other Graphs": Other_Graphs,
        # "DataFrame Demo": data_frame_demo
    }

    demo_name = st.sidebar.selectbox(
        "Choose a demo", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()
