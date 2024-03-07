
const Overlay = ({ restartGame, exitGame }) => (
  <div style={{ position: 'fixed', top: 0, left: 0, width: '100%', height: '100%', background: 'rgba(0, 0, 0, 0.5)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
    <div style={{ background: 'white', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
      <h2>Game Over!</h2>
      <p>Your score: {points}</p>
      <button onClick={restartGame}>Restart</button>
      <button onClick={exitGame}>Exit</button>
    </div>
  </div>
);

// Render the component to the overlay-root element
ReactDOM.render(<Overlay />, document.getElementById('overlay-root'));
