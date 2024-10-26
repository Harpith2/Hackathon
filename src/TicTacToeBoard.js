// TicTacToeBoard.js
import React, { useState } from 'react';
import axios from 'axios';
import './TicTacToeBoard.css';


const MemoryRecallBoard = () => {
    const [aiPrompt, setAiPrompt] = useState('');
    const [tiles, setTiles] = useState(Array(9).fill(null));
    
    // Predefined memory recall prompts for each tile
    const basePrompts = {
        1: "Tell me about a childhood memory that makes you smile.",
        2: "What was your favorite family tradition growing up?",
        3: "Describe your most memorable birthday celebration.",
        4: "When was the last time you felt truly proud of yourself?",
        5: "What's a special moment you shared with a friend?",
        6: "Tell me about a place you visited that left a lasting impression.",
        7: "What's a skill you learned that changed your life?",
        8: "Describe a moment when you overcame a challenge.",
        9: "What's a random act of kindness you'll never forget?"
    };

    const handleClick = async (tile) => {
        if (tiles[tile - 1]) {
            setAiPrompt('This memory has already been explored. Try another tile!');
            return;
        }

        

        const newTiles = [...tiles];
        newTiles[tile - 1] = '💭';
        setTiles(newTiles);

        try {
            const response = await axios.post('http://127.0.0.1:5000/generate_prompt', {
                prompt: `Generate a therapeutic memory recall question similar to: ${basePrompts[tile + 1]}. The question should be personal and emotional, focusing on positive memories and experiences.`,
                basePrompt: basePrompts[tile + 1]
            });

            setAiPrompt(response.data.prompt);
        } catch (error) {
            console.error('Error fetching prompt:', error);
            // Fallback to base prompt if API fails
            setAiPrompt(basePrompts[tile + 1]);
        }
    };

    return (
        <div className="container">
            <h1 className="title">Memory Lane</h1>
            <p className="subtitle">Click on a tile to explore your memories</p>
            <div className="board">
                {Array.from({ length: 9 }).map((_, index) => (
                    <div 
                        key={index} 
                        className={`tile ${tiles[index] ? 'explored' : ''}`}
                        onClick={() => handleClick(index + 1)}
                    >
                        {tiles[index] || '?'}
                    </div>
                ))}
            </div>
            {aiPrompt && (
                <div className="prompt-container">
                    <h2>Reflect on this:</h2>
                    <p className="memory-prompt">{aiPrompt}</p>
                </div>
            )}
        </div>
    );
};

export default MemoryRecallBoard;