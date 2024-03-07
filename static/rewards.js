const React = require('react');

const Rewards = ({ points }) => {
    // Render React component with points data
    return (
        React.createElement('div', null,
            React.createElement('p', null, `Points: ${points}`)
        )
    );
};

module.exports = Rewards;
