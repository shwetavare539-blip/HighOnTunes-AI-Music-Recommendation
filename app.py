import gradio as gr
from recommendation import recommend_songs
from song_sql_chatbot import ask_song_bot

custom_css = """
.gradio-container {
    background: linear-gradient(135deg, #121212, #2b1055, #000000);
    color: white;
}
#title {
    text-align: center;
}
button {
    font-weight: bold !important;
}
"""

with gr.Blocks(css=custom_css, title="HighOnTunes 🎵") as app:

    gr.Markdown(
        """
        <div id="title">
        <h1>HighOnTunes 🎵</h1>
        <h3>Because every emotion deserves a soundtrack.</h3>
        <p><b>Built by Shweta Vare ;) <b></p>
        """
        
    
    )

    with gr.Row():
        with gr.Column(scale=1):
            mood = gr.Dropdown(
                choices=["Chill", "Sad", "Happy", "Study", "Workout"],
                value="Chill",
                label="Select Mood"
            )

            language = gr.Dropdown(
                choices=["Any", "English", "Hindi"],
                value="Any",
                label="Select Language"
            )

            find_btn = gr.Button("Find My Soundtrack 🎧", variant="primary")

        with gr.Column(scale=2):
            output = gr.Dataframe(
                headers=["track_name","artist_name","mood","lanuage","Popularity"],
                label="Recommended Songs",
                interactive=False
            )

    gr.Markdown("## 🤖 Ask HighOnTunes Chatbot")

    with gr.Row():
        with gr.Column(scale=1):
            user_question = gr.Textbox(
                label="Tell me how you feel",
                placeholder="Example: I feel lowkey tired today",
                lines=4
            )

            ask_btn = gr.Button("Ask Chatbot", variant="primary")

        with gr.Column(scale=2):
            bot_output = gr.Dataframe(
                headers=["track_name","artist_name","mood","popularity"],
                label="Chatbot Recommended Songs",
                interactive=False
            )

    find_btn.click(
        fn=recommend_songs,
        inputs=[mood, language],
        outputs=output
    )

    ask_btn.click(
        fn=ask_song_bot,
        inputs=user_question,
        outputs=bot_output
    )

app.launch(share=True)
