import React, { useState } from 'react';
import {
  DatePicker, Card, Badge, Descriptions, Tag, Tooltip,
  Row, Col, Statistic, Space
} from 'antd';
import HoverableTag from './HoverableTag';
import { InfoCircleOutlined } from '@ant-design/icons';
const { Meta } = Card;

// Component for the Company Card
const CompanyCard = ({ 
  name, description, address, marketCap, share,
  revenue, profit, management, totalAssets, debt, firstSkill, industries,
  businessQuality, priceQuality, riskQuality
}) => {
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
          {industries.map((industry, index) => (
            <HoverableTag content={industry} />
          ))}
          <br/><br/><br/>
          <Row gutter={16}>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Vốn hoá thị trường
                    <Tooltip title="Vốn hoá thị trường là tổng giá trị của công ty được tính bằng cách nhân giá cổ phiếu hiện tại với số lượng cổ phiếu đang lưu hành.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={marketCap}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Doanh Thu
                    <Tooltip title="Doanh thu là tổng số tiền thu được từ bán hàng hoặc cung cấp dịch vụ trước khi trừ bất kỳ chi phí nào.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={revenue}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Lợi Nhuận
                    <Tooltip title="Lợi nhuận là tổng thu nhập ròng của công ty sau khi đã trừ đi tất cả chi phí.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={profit}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
          </Row>
          <br/>
          <Row gutter={16}>
          <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Số lượng cổ phiếu lưu hành
                    <Tooltip title="Được tính bằng: Khối lượng cổ phiếu đang niêm yết + Khối lượng cổ phiếu chưa niêm yết - Cổ phiếu quỹ">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={share}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Tài Sản
                    <Tooltip title="Tài sản là tổng giá trị của tất cả các tài sản mà công ty sở hữu.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={totalAssets}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Nợ
                    <Tooltip title="Nợ là tổng số tiền mà công ty phải trả cho các khoản vay hoặc các nghĩa vụ tài chính khác.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={debt}
                valueStyle={{ fontSize: '12px' }}
              />
            </Col>
          </Row>
          <br/>
          <Row gutter={16}>
          <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Chất lượng doanh nghiệp
                    <Tooltip title="Chất lượng doanh nghiệp là yếu tố quan trọng trong đầu tư. Đầu tư vào những cổ phiếu có chất lượng Tốt và Rất Tốt sẽ an toàn và hiệu quả hơn là đầu tư vào những cổ phiếu có chất lượng Không ổn định.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={businessQuality}
                valueStyle={{ fontSize: '12px', fontWeight: 'bold', color: '#faad14' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Định giá
                    <Tooltip title="Những cổ phiếu có định giá Hấp dẫn (đang được giao dịch thấp hơn giá trị nội tại với biên an toàn đủ lớn) thường là những cơ hội đầu tư tuyệt vời.
Tuy nhiên, hãy kết hợp thêm các yếu tố khác như chất lượng doanh nghiệp, rủi ro thị trường… để đánh giá xem có nên đầu tư vào cổ phiếu đó hay không?
Hãy luôn tìm hiểu kỹ về công ty và nền tảng tài chính trước khi quyết định đầu tư vào cổ phiếu đó.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={priceQuality}
                valueStyle={{ fontSize: '12px', fontWeight: 'bold', color: 'green' }}
              />
            </Col>
            <Col span={8}>
              <Statistic
                title={
                  <span style={{ fontSize: '12px' }}>
                    Rủi ro
                    <Tooltip title="Đầu tư vào những cổ phiếu có rủi ro Thấp hoặc Trung bình sẽ an toàn hơn, giúp bạn giảm thiểu khả năng mất một phần, hoặc toàn bộ số tiền đầu tư của mình khi đầu tư cổ phiếu.">
                      <InfoCircleOutlined style={{ marginLeft: 5, color: 'rgba(0,0,0,.45)' }} />
                    </Tooltip>
                  </span>
                }
                value={riskQuality}
                valueStyle={{ fontSize: '12px', fontWeight: 'bold', color: 'green' }}
              />
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
  marketCap: "48,899T",
  management: "Đội ngũ quản lý từ nhà nước",
  totalAssets: "27.1k tỷ",
  debt: "1.4k tỷ",
  price: "36.80",
  firstSkill: {
    "name": "Liên doanh sản xuất Ô tô",
    "description": "Chiếm 50% thị trường ô tô của Việt Nam (Toyota, Honda)"
  },
  share: "1,328,800,000",
  industries: ["Công nghiệp", "Máy móc, thiết bị nặng và đóng tàu"],
  businessQuality: "Trung bình",
  priceQuality: "Hấp dẫn",
  riskQuality: "Thấp"
}

export default CompanyCard;
export { BusinessData };
