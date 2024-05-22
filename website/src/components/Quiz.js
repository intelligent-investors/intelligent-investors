import {
  Card
} from 'antd';
import React, { useState } from 'react';
const { Meta } = Card;

// Component for the Quiz
const Quiz = ({ 
  question, options, correctAnswer
}) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isCorrectAnswer, setIsCorrectAnswer] = useState(false);

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleSubmit = () => {
    setIsSubmitted(true);
    setIsCorrectAnswer(selectedOption === correctAnswer);
  };

  return (
    <div>
      <h2>{question}</h2>
      <form>
        {options.map((option, index) => (
          <div key={index}>
            <label>
              <input
                type="radio"
                value={option}
                checked={selectedOption === option}
                onChange={handleOptionChange}
                disabled={isSubmitted}
              />
              {option}
            </label>
          </div>
        ))}
      </form>
      <button onClick={handleSubmit} disabled={isSubmitted}>Submit</button>
      {isSubmitted && (
        <div>
          {isCorrect ? <p>Correct!</p> : <p>Incorrect. The correct answer is {correctAnswer}.</p>}
        </div>
      )}
    </div>
  );
};

export default Quiz;