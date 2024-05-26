import { Button, Card } from 'antd';
import React, { useState } from 'react';
import '../css/quiz.css';


const Quiz = ({ questions }) => {
  const [answers, setAnswers] = useState(Array(questions.length).fill(null));
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleOptionChange = (questionIndex, selectedOption) => {
    const newAnswers = [...answers];
    newAnswers[questionIndex] = selectedOption;
    setAnswers(newAnswers);
  };

  const handleSubmit = () => {
    setIsSubmitted(true);
  };

  const getAnswerLabel = (index) => String.fromCharCode(65 + index);

  return (
    <Card title="Quiz">
      {questions.map((question, index) => (
        <div key={index} className="question-container">
          <p>{index + 1}. {question.question}</p>
          <form>
            {question.answer.map((option, i) => (
              <div key={i}>
                <label>
                  <input
                    type="radio"
                    value={option.value}
                    checked={answers[index] === option.value}
                    onChange={() => handleOptionChange(index, option.value)}
                    disabled={isSubmitted}
                  />
                  {getAnswerLabel(i)}. {option.value}
                </label>
              </div>
            ))}
          </form>
          {isSubmitted && (
            <p className={answers[index] === question.answer.find(opt => opt.correct === "true").value ? "correct" : "incorrect"}>
              {answers[index] === question.answer.find(opt => opt.correct === "true").value
                ? "Correct!"
                : `Incorrect. The correct answer is ${question.answer.find(opt => opt.correct === "true").value}.`}
              <br />
              {question.answer.find(opt => opt.correct === "true").explaination}
            </p>
          )}
          {index < questions.length - 1 && <hr className="divider" />}
        </div>
      ))}
      {!isSubmitted && (
        <Button type="primary" onClick={handleSubmit} style={{ marginTop: '20px' }}>
          Submit
        </Button>
      )}
    </Card>
  );
};

export default Quiz;