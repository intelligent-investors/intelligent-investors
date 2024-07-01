import { Button, Card } from 'antd';
import React, { useState } from 'react';
import Latex from 'react-latex-next';

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

  let questionCount = 0;

  return (
    <Card title="Quiz">
      {questions.map((question, index) => {
        const isQuestion = !!question.question;

        if (isQuestion) questionCount += 1;

        return (
          <div key={index} style={{ marginBottom: '20px' }}>
            {isQuestion ? (
              <>
                <div>{questionCount}. <Latex>{question.question}</Latex></div>
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
                  <p style={{ color: answers[index] === question.answer.find(opt => opt.correct === "true").value ? '#52c41a' : '#f5222d' }}>
                    {answers[index] === question.answer.find(opt => opt.correct === "true").value
                      ? "Correct!"
                      : `Incorrect. The correct answer is ${question.answer.find(opt => opt.correct === "true").value}.`}
                    <br />
                    {question.answer.find(opt => opt.correct === "true").explanation}
                  </p>
                )}
              </>
            ) : (
              <div>{question.notes}</div>
            )}
            {index < questions.length - 1 && <hr style={{ margin: '20px 0', border: 0, borderTop: '1px solid #d9d9d9' }} />}
          </div>
        );
      })}
      {!isSubmitted && (
        <Button type="primary" onClick={handleSubmit} style={{ marginTop: '20px' }}>
          Submit
        </Button>
      )}
    </Card>
  );
};

export default Quiz;