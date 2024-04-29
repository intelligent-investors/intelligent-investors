import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function GoalSetting() {
  const [balance, setBalance] = useState(100000);
  const [income, setIncome] = useState(36000);
  const [interestRate, setInterestRate] = useState(6);
  const [dataPoints, setDataPoints] = useState([]);

  const calculateBalance = () => {
    let yearlyBalance = balance;
    const rates = [];
    for (let year = 1; year <= 20; year++) {
      yearlyBalance += income + (yearlyBalance * (interestRate / 100));
      rates.push(Math.round(yearlyBalance));
    }
    setDataPoints(rates);
  };

  useEffect(() => {
    calculateBalance();
  }, []); // Dependency array is empty, so it runs once on mount

  const data = {
    labels: Array.from({ length: 20 }, (_, i) => new Date().getFullYear() + i),
    datasets: [
      {
        label: 'Balance',
        data: dataPoints,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.5)',
      },
    ],
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <p><b>Goal Setting Example</b></p>
      <label htmlFor="initialBalance">Initial Balance:</label>
      <input
        id="initialBalance"
        type="number"
        value={balance}
        onChange={(e) => setBalance(parseFloat(e.target.value))}
      />
      <label htmlFor="annualIncome">Annual Income:</label>
      <input
        id="annualIncome"
        type="number"
        value={income}
        onChange={(e) => setIncome(parseFloat(e.target.value))}
      />
      <label htmlFor="interestRate">Interest Rate (%):</label>
      <input
        id="interestRate"
        type="number"
        value={interestRate}
        onChange={(e) => setInterestRate(parseFloat(e.target.value))}
      />
      <button onClick={calculateBalance}>Calculate</button>
      {dataPoints.length > 0 && <Line data={data} />}
    </div>
  );
}
