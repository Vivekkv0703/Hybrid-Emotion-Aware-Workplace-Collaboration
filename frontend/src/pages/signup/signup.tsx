import React, { useState } from 'react'
import {
  Layout,
  Form,
  Input,
  Button,
  Typography,
  Upload,
  message,
  theme,
} from 'antd'
import {
  UploadOutlined,
  BankOutlined,
  GlobalOutlined,
  AppstoreOutlined,
  EnvironmentOutlined,
  FlagOutlined,
  UserAddOutlined,
} from '@ant-design/icons'

const { Title, Text } = Typography
const { Content } = Layout

export function Signup() {
  const [loading, setLoading] = useState(false)
  const { token } = theme.useToken()

  interface SignupValues {
    companyName: string
    domain?: string
    industry?: string
    location?: string
    state?: string
    logo?: any
  }

  const onFinish = async (values: SignupValues) => {
    setLoading(true)
    try {
      await new Promise((res) => setTimeout(res, 1000))
      message.success(`Welcome, ${values.companyName}!`)
      console.log('Form data:', values)
    } catch {
      message.error('Signup failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout style={{ minHeight: '100vh', padding: '10px' }}>
      <Content
        style={{
          flex: 1,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: token.colorBgLayout,
        }}
      >
        <div
          style={{
            width: 800,
            padding: '48px 40px',
            borderRadius: 16,
            boxShadow: '0 8px 24px rgba(0,0,0,0.12)',
            backgroundColor: token.colorBgContainer,
          }}
        >
          <Title level={2} style={{ textAlign: 'center', marginBottom: 8 }}>
            Create Your Account
          </Title>
          <Text
            type="secondary"
            style={{ display: 'block', textAlign: 'center', marginBottom: 32 }}
          >
            Fill in your company details to get started
          </Text>

          <Form
            name="signup"
            layout="vertical"
            onFinish={onFinish}
            requiredMark={false}
          >
            <div className='flex justify-between  gap-8'>
                <div className='w-[400px]'>
                    <Form.Item
                    name="companyName"
                    label="Company Name"
                    rules={[{ required: true, message: 'Please enter your company name' }]}
                    >
                    <Input
                        prefix={<BankOutlined />}
                        placeholder="Acme Inc."
                        size="large"
                    />
                    </Form.Item>

                    <Form.Item name="domain" label="Domain">
                    <Input
                        prefix={<GlobalOutlined />}
                        placeholder="acme.com"
                        size="large"
                    />
                    </Form.Item>

                    <Form.Item name="industry" label="Industry">
                    <Input
                        prefix={<AppstoreOutlined />}
                        placeholder="Technology"
                        size="large"
                    />
                    </Form.Item>

                    <Form.Item name="location" label="Location">
                    <Input
                        prefix={<EnvironmentOutlined />}
                        placeholder="City, Country"
                        size="large"
                    />
                    </Form.Item>

                    <Form.Item name="state" label="State">
                    <Input
                        prefix={<FlagOutlined />}
                        placeholder="State/Province"
                        size="large"
                    />
                    </Form.Item>
                </div>
                <div className='flex flex-col items-center justify-center h-full'>
                    <Form.Item
                        name="logo"
                        label="Company Logo"
                        valuePropName="fileList"
                        getValueFromEvent={(e) => (Array.isArray(e) ? e : e?.fileList)}
                    >
                    <Upload.Dragger
                        name="logo"
                        accept="image/*"
                        beforeUpload={() => false} 
                        maxCount={1}  
                    >
                        <p className="ant-upload-drag-icon">
                        <UploadOutlined />
                        </p>
                        <p className="ant-upload-text">
                        Click or drag image to upload
                        </p>
                        <p className="ant-upload-hint">
                        PNG, JPG, or SVG up to 2 MB
                        </p>
                    </Upload.Dragger>
                    </Form.Item>
                </div>
            </div>
            <Form.Item>
              <Button
                type="primary"
                htmlType="submit"
                size="large"
                block
                loading={loading}
                icon={<UserAddOutlined />}
              >
                Sign Up
              </Button>
            </Form.Item>
          </Form>

          <Text
            type="secondary"
            style={{ display: 'block', textAlign: 'center', marginTop: 24 }}
          >
            Already have an account? <a href="/login">Log in</a>
          </Text>
        </div>
      </Content>
    </Layout>
  )
}
