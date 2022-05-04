import "./App.css";
import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const subtitles = [
    {
      text: "Back here LIVE at the waterfront village",
      startTime: 0,
      endTime: 2.75,
    },
    {
      text: "with my friend the zombie, Jonathan",
      startTime: 2.75,
      endTime: 5.21,
    },
    {
      text: "You're looking good! Jonathan just got an awesome face-paint job, what do you think?",
      startTime: 5.21,
      endTime: 8.78,
    },
    {
      text: "I LIKE TURTLES!!!",
      startTime: 8.78,
      endTime: 10.18,
    },
    {
      text: "...Alright! You're a great zombie.",
      startTime: 10.18,
      endTime: 12.9,
    },
    {
      text: "And good times here at the Waterfront Village, open for the next 11 days ....",
      startTime: 12.9,
      endTime: 17.08,
    },
  ];

  const checkTimeUpdate = (event) => {
    const s = subtitles.find((subtitle) => {
      return (
        subtitle.startTime <= event.target.currentTime &&
        subtitle.endTime >= event.target.currentTime
      );
    });
    setText(s.text);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Zombie Kid Likes Turtles</p>
      </header>
      <video
        onTimeUpdate={checkTimeUpdate}
        controls
        width="30%"
        src="https://cdn.kapwing.com/samples/5c4231d44d02e3ffa24640d6.mp4"
      ></video>
      <div> {text}</div>
    </div>
  );
}

export default App;
