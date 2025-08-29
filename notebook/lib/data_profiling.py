from IPython.display import display
from ydata_profiling import ProfileReport
import os
import webbrowser

# -------------------------

def profile_data(df,
                 file_name='data_profiling',
                 report_title='YData Profiling Report',
                 show=False):
    """
    Profiles the given DataFrame and generates an HTML report.

    Parameters:
        - df (pd.DataFrame): The DataFrame to profile.
        - file_name (str): The name of the output HTML file (without extension). Default is 'data_profiling'.
        - report_title (str): The title of the report. Default is 'YData Profiling Report'.
        - show (bool): Whether to display the report in the notebook. Default is False.
    """

    # Ensuring the output directory exists
    WORK_DIR = os.path.abspath('../res/data-profiling')
    if not os.path.exists(WORK_DIR):
        os.makedirs(WORK_DIR)

    # Creating the report
    OUT_FILE = os.path.join(WORK_DIR, f"{file_name}.html")
    profile = ProfileReport(df, explorative=True, title=report_title)
    profile.to_file(OUT_FILE)

    # Display in the notebook if required
    if show:
        display(profile)

    # -------------------------

    # Opening the report in the default web browser
    webbrowser.open(f"file://{OUT_FILE}")
