import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import trophy from './trophy.png'


function App() {

  const [points, setPoints] = useState(0)
  const [user, setUser] = useState("")

  useEffect(() => {
      fetch('/rewards')
        .then(res => {
          if (!res.ok) {
            throw new Error('Network response was not ok');
          }
          return res.text();
        })
        .then(data => {
          console.log(data); // Log the response
          const parsedData = JSON.parse(data); // Attempt to parse the response as JSON
          setPoints(parsedData.points);
          setUser(parsedData.user)
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
        });

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <h1>Game Over {user}!</h1>
      <img src={trophy} className="trophy" alt="trophy" style={{ width: '100px', height: 'auto' }} />
        
        <p> Total Points: {points} </p>
      </header>
    </div>
  );
}

export default App;
