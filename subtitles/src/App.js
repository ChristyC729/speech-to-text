import './App.css';
import SampleVideo from './subs/sample1.mp4'
import EnglishSubs from './subs/sample1.vtt'
import SwedishSubs from './subs/sample2.vtt'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Subtitle Practice</p>
      </header>
      <video id='video' className="video" controls src={SampleVideo}>
        <track id='english' kind='subtitles' srclang='English' src={EnglishSubs} default/>
        <track id='swedish' kind='subtitles' srclang='Swedish' src={SwedishSubs}/>
      </video>
    </div>
  );
}

export default App;
