"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[1089],{967:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>x,contentTitle:()=>p,default:()=>j,frontMatter:()=>h,metadata:()=>y,toc:()=>g});var n=a(4848),l=a(8453),i=a(6540),s=a(9421),r=a(4692),o=a(5100),m=a(1223),c=a(6405),d=a(7734);const u=()=>{const e=1e9,[t,a]=(0,i.useState)(e),[l,u]=(0,i.useState)(8),[h,p]=(0,i.useState)(36),[y,x]=(0,i.useState)(null),[g,f]=(0,i.useState)([]),j=e=>{const t=parseFloat(e);return 0===t||Math.abs(t)<5e-5?"0":new Intl.NumberFormat("en-US",{style:"decimal",minimumFractionDigits:2,maximumFractionDigits:2}).format(e)};return(0,n.jsxs)("div",{children:[(0,n.jsxs)(s.A,{labelCol:{span:8},wrapperCol:{span:16},children:[(0,n.jsx)(s.A.Item,{name:"Loan Amount",label:"Loan Amount",children:(0,n.jsx)(r.A,{style:{width:400},formatter:e=>`${e}`.replace(/\B(?=(\d{3})+(?!\d))/g,","),parser:e=>e.replace(/\$\s?|(,*)/g,""),defaultValue:e,placeholder:"S\u1ed1 ti\u1ec1n vay",onChange:a})}),(0,n.jsx)(s.A.Item,{name:"Interest Rate",label:"Interest Rate",children:(0,n.jsx)(o.A,{style:{width:400},placeholder:"L\xe3i su\u1ea5t (%)",defaultValue:8,onChange:e=>u(e.target.value)})}),(0,n.jsx)(s.A.Item,{name:"Loan Term",label:"Loan Term",children:(0,n.jsx)(o.A,{style:{width:400},placeholder:"Th\u1eddi gian vay (th\xe1ng)",defaultValue:36,onChange:e=>p(e.target.value)})}),(0,n.jsx)(s.A.Item,{wrapperCol:{offset:8,span:16},children:(0,n.jsx)(m.A,{children:(0,n.jsx)(c.Ay,{type:"primary",htmlType:"submit",onClick:()=>{const e=parseFloat(t),a=parseFloat(l)/100/12,n=parseInt(h),i=e*(a*Math.pow(1+a,n))/(Math.pow(1+a,n)-1),s=new Intl.NumberFormat("en-US",{style:"decimal",minimumFractionDigits:2,maximumFractionDigits:2}).format(i);x(s),((e,t,a)=>{let n=e;const l=[];let i,s,r;l.push({key:0,month:0,principalPayment:"",interestPayment:"",totalPayment:"",remainingBalance:j(e)});for(let o=1;o<=a;o++)i=n*t,s=e/a,r=i+s,n-=s,l.push({key:o,month:o,principalPayment:j(s),interestPayment:j(i),totalPayment:j(r),remainingBalance:j(n)});f(l)})(e,a,n)},children:"Calculate"})})})]}),(0,n.jsxs)("div",{style:{display:"flex",justifyContent:"center",alignItems:"center",flexDirection:"column"},children:[y&&(0,n.jsxs)("p",{children:["Monthly Payment: ",y]}),(0,n.jsx)(d.A,{columns:[{title:"Month",dataIndex:"month",key:"month"},{title:"Principal Payment",dataIndex:"principalPayment",key:"principalPayment"},{title:"Interest Payment",dataIndex:"interestPayment",key:"interestPayment"},{title:"Total Payment",dataIndex:"totalPayment",key:"totalPayment"},{title:"Remaining Balance",dataIndex:"remainingBalance",key:"remainingBalance"}],dataSource:g,pagination:{pageSize:360}})]})]})},h={},p="Real Estate Tool",y={id:"what-to-invest-in/real-estate-tool",title:"Real Estate Tool",description:"",source:"@site/docs/what-to-invest-in/real-estate-tool.mdx",sourceDirName:"what-to-invest-in",slug:"/what-to-invest-in/real-estate-tool",permalink:"/intelligent-investors/website/build/docs/what-to-invest-in/real-estate-tool",draft:!1,unlisted:!1,tags:[],version:"current",frontMatter:{}},x={},g=[];function f(e){const t={h1:"h1",...(0,l.R)(),...e.components};return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(t.h1,{id:"real-estate-tool",children:"Real Estate Tool"}),"\n","\n",(0,n.jsx)(u,{})]})}function j(e={}){const{wrapper:t}={...(0,l.R)(),...e.components};return t?(0,n.jsx)(t,{...e,children:(0,n.jsx)(f,{...e})}):f(e)}}}]);