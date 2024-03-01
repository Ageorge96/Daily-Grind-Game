import React, { useEffect } from 'react';

const Rewards = ({ onClose }) => {
    useEffect(() => {
        const handleCollision = async () => {
            try {
                const response = await fetch('http://localhost:5000/rewards', {
                    method: 'GET',
                });

                if (response.ok) {
                    const scriptContent = await response.text();

                    // Create a script element and append it to the body
                    eval(scriptContent)

                    console.log('Collision detected in React! Show rewards.');
                    onClose();  // Close the rewards component if needed
                } else {
                    console.error('Failed to trigger rewards:', response.statusText);
                }
            } catch (error) {
                console.error('Error:', error.message);
            }
        };

        const ws = new WebSocket("ws://localhost:8000");

        ws.onmessage = (event) => {
            if (event.data === "collision_ack") {
                handleCollision();
            }
        };

        return () => {
            ws.close();
        };
    }, [onClose]);

    return (
        <div className="popup">
            <h2>Game Over</h2>
            <button onClick={onClose}>Exit</button>
        </div>
    );
};

export default Rewards;
