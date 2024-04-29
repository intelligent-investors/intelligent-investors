import React, { useState } from 'react';

export default function Cashflow({ lang = 'en' }) {
  const people = [
    { name: "Tiana", role: "Teacher", salary: 3300 },
    { name: "David", role: "Doctor", salary: 13200 },
    { name: "Eric", role: "Engineer", salary: 4500 },
    { name: "Jenifer", role: "Janitor", salary: 1600 },
    { name: "Levi", role: "Lawyer", salary: 7500 },
  ];

  const translations = {
    en: {
      title: "Cashflow Example",
      name: "Name",
      profession: "Profession",
      salary: "Salary",
      changeButton: "Change Person"
    },
    vi: {
      title: "Ví dụ về dòng tiền",
      name: "Tên",
      profession: "Nghề nghiệp",
      salary: "Lương",
      changeButton: "Đổi người"
    }
  };

  // Function to select a random person from the people array
  const getRandomPerson = (people) => {
    return people[Math.floor(Math.random() * people.length)];
  };

  // Use useState to manage the random person's state
  const [person, setPerson] = useState(() => getRandomPerson(people));

  // Function to update the person state to a new random person
  const handleChangePerson = () => {
    let newPerson;
    do {
      newPerson = getRandomPerson(people);
    } while (newPerson.name === person.name); // Keep selecting until a different person is found
    setPerson(newPerson);
  };

  const { title, name, profession, salary, changeButton } = translations[lang];

  return (
    <div style={{ textAlign: 'center' }}>
      <b>{title}</b>
      <table style={{ margin: 'auto', borderCollapse: 'collapse', display: 'flex', justifyContent: 'center' }}>
        <tbody>
          <tr>
            <th style={{ border: '1px solid black', padding: '8px' }}>{name}</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>{profession}</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>{salary}</th>
          </tr>
          <tr>
            <td style={{ border: '1px solid black', padding: '8px' }}>{person.name}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}>{person.role}</td>
            <td style={{ border: '1px solid black', padding: '8px', color: 'red' }}>${person.salary.toLocaleString()}</td>
          </tr>
        </tbody>
      </table>
      <button onClick={handleChangePerson}>{changeButton}</button>
    </div>
  );
}