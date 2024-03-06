import React, { useEffect, useState } from 'react';
import axios from 'axios'
import '../static/rewards.css';

const Rewards = () => {
    const [points, setPoints] = useState('');

    useEffect(() => {
        axios.get('http://localhost:5000/rewards')
            .then(response => {
                console.log("setting points")
                setPoints(response.data.points);
            })
            .catch(error => {
                console.error('Error fetching rewards:', error);
            });
    }, []);

    return (
        <div>
            <p>Points: {points}</p>
        </div>
    );
};


export default Rewards;
