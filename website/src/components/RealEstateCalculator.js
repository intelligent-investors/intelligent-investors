import React, { useState } from 'react';
import { InputNumber, Input, Button, Space, Form, Table } from 'antd';

const RealEstateCalculator = () => {
  const defaultLoanAmount = 1000000000;
  const defaultInterestRate = 8;
  const defaultLoanTerm = 36;
  const [loanAmount, setLoanAmount] = useState(defaultLoanAmount);
  const [interestRate, setInterestRate] = useState(defaultInterestRate);
  const [loanTerm, setLoanTerm] = useState(defaultLoanTerm);
  const [monthlyPayment, setMonthlyPayment] = useState(null);
  const [schedule, setSchedule] = useState([]);

  const generateAmortizationSchedule = (principal, rate, term) => {
    let balance = principal;
    const tempSchedule = [];
    let interestPayment, principalPayment, totalPayment;
    tempSchedule.push({
      key: 0,
      month: 0,
      principalPayment: "",
      interestPayment: "",
      totalPayment: "",
      remainingBalance: formatNumber(principal)
    })
    for (let i = 1; i <= term; i++) {
      interestPayment = balance  * rate;
      principalPayment = principal / term;
      totalPayment = interestPayment + principalPayment;

      balance -= principalPayment;

      tempSchedule.push({
        key: i,
        month: i,
        principalPayment: formatNumber(principalPayment),
        interestPayment: formatNumber(interestPayment),
        totalPayment: formatNumber(totalPayment),
        remainingBalance: formatNumber(balance)
      });
    }

    setSchedule(tempSchedule);
  };

  const formatNumber = (number) => {
    const num = parseFloat(number);
    if(num === 0 || Math.abs(num) < 0.00005) return '0';
    return new Intl.NumberFormat('en-US', {
      style: 'decimal',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(number);
  }

  // Function to calculate the monthly payment
  const calculatePayment = () => {
    const principal = parseFloat(loanAmount);
    const monthlyInterestRate = parseFloat(interestRate) / 100 / 12;
    const numberOfPayments = parseInt(loanTerm);

    // Formula to calculate the monthly payment
    const payment = principal * (monthlyInterestRate * Math.pow((1 + monthlyInterestRate), numberOfPayments)) / (Math.pow((1 + monthlyInterestRate), numberOfPayments) - 1);
    const formattedPayment = new Intl.NumberFormat('en-US', {
      style: 'decimal',
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    }).format(payment);

    setMonthlyPayment(formattedPayment);
    generateAmortizationSchedule(principal, monthlyInterestRate, numberOfPayments);
  };

  const layout = {
    labelCol: {
      span: 8,
    },
    wrapperCol: {
      span: 16,
    },
  };
  const tailLayout = {
    wrapperCol: {
      offset: 8,
      span: 16,
    },
  };

  const columns = [
    {
      title: 'Month',
      dataIndex: 'month',
      key: 'month',
    },
    {
      title: 'Principal Payment',
      dataIndex: 'principalPayment',
      key: 'principalPayment',
    },
    {
      title: 'Interest Payment',
      dataIndex: 'interestPayment',
      key: 'interestPayment',
    },
    {
      title: 'Total Payment',
      dataIndex: 'totalPayment',
      key: 'totalPayment',
    },
    {
      title: 'Remaining Balance',
      dataIndex: 'remainingBalance',
      key: 'remainingBalance',
    },
  ];

  return (
    <div>
      <Form {...layout}>
        <Form.Item name="Loan Amount" label="Loan Amount">
          <InputNumber
              style={{ width: 400 }}
              formatter={value => `${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')}
              parser={value => value.replace(/\$\s?|(,*)/g, '')}
              defaultValue={defaultLoanAmount}
              placeholder="Số tiền vay"
              onChange={setLoanAmount}
            />
        </Form.Item>
        <Form.Item name="Interest Rate" label="Interest Rate">
          <Input
              style={{ width: 400 }}
              placeholder="Lãi suất (%)"
              defaultValue={defaultInterestRate}
              onChange={e => setInterestRate(e.target.value)}
            />
        </Form.Item>
        <Form.Item name="Loan Term" label="Loan Term">
          <Input
              style={{ width: 400 }}
              placeholder="Thời gian vay (tháng)"
              defaultValue={defaultLoanTerm}
              onChange={e => setLoanTerm(e.target.value)}
            />
        </Form.Item>
        <Form.Item {...tailLayout}>
          <Space>
            <Button type="primary" htmlType="submit" onClick={calculatePayment}>
              Calculate
            </Button>
          </Space>
        </Form.Item>
      </Form>

      <div style={{ display: 'flex', justifyContent: 'center', 
        alignItems: 'center',
        flexDirection: 'column' }}>
        {monthlyPayment && <p>Monthly Payment: {monthlyPayment}</p>}
        
        <Table columns={columns} dataSource={schedule}
          pagination={{ pageSize: 360 }}
        />  
      </div>
    </div>
  );
};

export default RealEstateCalculator;