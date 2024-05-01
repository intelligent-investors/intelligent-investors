import React from 'react';

// Styles for the Pokémon-style card
const cardStyle = {
  background: 'linear-gradient(135deg, #9DCEFF 0%, #92A3FD 100%)', // Gradient background
  width: '330px',
  height: '460px',
  margin: '20px auto',
  padding: '20px',
  border: '1px solid #ddd',
  borderRadius: '10px',
  boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
  color: '#003A70', // Dark blue text color for better visibility
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'space-between'
};

const headerStyle = {
  textAlign: 'center',
  fontWeight: 'bold',
  fontSize: '24px'
};

const contentStyle = {
  margin: '20px 0',
};

const footerStyle = {
  textAlign: 'center',
  fontSize: '14px'
};

// Component for the Company Card
const CompanyCard = ({ name, description, address }) => {
  return (
    <div style={cardStyle}>
      <div style={headerStyle}>{name}</div>
      <div style={contentStyle}>
        <p>{description}</p>
        <address>{address}</address>
      </div>
      <div style={footerStyle}>Contact Us</div>
    </div>
  );
};

const BusinessData = {
  name: "Công ty Máy Động lực và Máy Nông nghiệp Việt Nam (VEAM)",
  description: "Chuyên sản xuất và lắp ráp động cơ diesel nhỏ và máy nông nghiệp.",
  address: "Bộ Công Thương, 655 Phố Vũ Tông Phan, Khương Đình, Thanh Xuân, Hà Nội, Việt Nam"
}

export default CompanyCard;
export { BusinessData };