import React from 'react';
import {
  DatePicker, Card, Badge, Descriptions,
  Row, Col, Statistic, Space
} from 'antd';

const { Meta } = Card;

// Component for the Company Card
const CompanyCard = ({ name, description, address, revenue, profit, management, totalAssets, debt, firstSkill }) => {
  const items = [
    {
      key: '1',
      label: 'Địa chỉ',
      children: address,
    },
    {
      key: '2',
      label: 'Thành lập',
      children: '1990',
    },
    {
      key: '3',
      label: 'Niêm yết',
      children: '2018',
    },
    {
      key: '4',
      label: 'Nhân sự',
      children: '716',
    },
  ];
  return (
    <div>
      <Badge.Ribbon text="Cổ tức">
        <Card hoverable>
          <Meta title={name} description={description} />
          <br/>
          <Row gutter={16}>
            <Col span={12}>
              <Statistic title="Doanh Thu (VND)" value={revenue} />
            </Col>
            <Col span={12}>
              <Statistic title="Lợi Nhuận (VND)" value={profit}/>
            </Col>
          </Row>
          <br/>
          <Row gutter={16}>
            <Col span={12}>
              <Statistic title="Tài Sản (VND)" value={totalAssets} />
            </Col>
            <Col span={12}>
              <Statistic title="Nợ (VND)" value={debt}/>
            </Col>
          </Row>
          <br/>
          <Col span={20}>
            <li>
              <ul>Sở hữu 30% Honda Việt Nam (chiếm 90% thị phần xe máy VN và top 5 ô tô)</ul>
              <ul>Sở hữu 20% Toyota Việt Nam (top 3 ô tô ở Việt Nam)</ul>
              <ul>Sở hữu 25% Ford Việt Nam (nhà sản xuất ô tô hàng đầu)</ul>
              <ul>1 năm nhận cổ tức 5,000-7,000 tỷ đồng tại các công ty liên doanh, tiền mặt trong tài khoản lớn hơn vốn điều lệ</ul>
              <ul>Tỷ suất cổ tức lớn hơn 10.46% ổn định và bền vững (chín muồi); Có thể tăng trưởng khi ô tô tiêu thụ nhanh trong tương lai</ul>
              <ul>Rủi ro: Phụ thuộc hoàn toàn vào công ty liên doanh; Hoạt động kinh doanh bản thân công ty mẹ kém</ul>
            </li>
          </Col>
          
          <br/>
          <Descriptions bordered={false} items={items} column={1}/>
        </Card>
      </Badge.Ribbon>
    </div>
  );
};

const BusinessData = {
  name: "VEAM",
  description: "Chuyên sản xuất và lắp ráp động cơ diesel nhỏ và máy nông nghiệp.",
  address: "Bộ Công Thương, 655 Phố Vũ Tông Phan, Khương Đình, Thanh Xuân, Hà Nội, Việt Nam",
  revenue: "3.8k tỷ",
  profit: "6.2k tỷ",
  management: "Đội ngũ quản lý từ nhà nước",
  totalAssets: "27.1k tỷ",
  debt: "1.4k tỷ",
  firstSkill: {
    "name": "Liên doanh sản xuất Ô tô",
    "description": "Chiếm 50% thị trường ô tô của Việt Nam (Toyota, Honda)"
  }
}

export default CompanyCard;
export { BusinessData };
