import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import trophy from './trophy.png'


function App() {

  const [points, setPoints] = useState(0)
  const [user, setUser] = useState("")
  const [exp, setExp] = useState(0)
  const [money, setMoney] = useState(0)
  const [statsVisible, setStatsVisible] = useState(false);

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
          console.log("data", parsedData)
          setPoints(parsedData.points);
          setExp(parsedData.exp)
          setMoney(parsedData.money)
          setUser(parsedData.user)
          setStatsVisible(true);
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
      {statsVisible && (
      <div className="stats" >
        <h3 className="stat" >Total Points: {points} </h3>
        <h3 className="stat" > Exp: {exp} </h3>
        <h3 className="stat" > Money: £{money} </h3>
        </div>
      )}
      </header>
      </div>
  );
}

export default App;
