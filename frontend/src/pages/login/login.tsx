import React, { useState } from "react";
import { Layout, Form, Input, Button, Typography, message, theme } from "antd";
import { UserOutlined, LockOutlined, LoginOutlined } from "@ant-design/icons";

const { Title, Text } = Typography;
const { Content } = Layout;

export function Login() {
  const [loading, setLoading] = useState(false);
  const { token } = theme.useToken();

  interface LoginValues {
    email: string;
    password: string;
    company_id: string;
  }

  const onFinish = async (values: LoginValues) => {
    setLoading(true);
    try {
      const response = await fetch(
        `/api/core/companies/${values.company_id}/employees/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: values.email,
            password: values.password,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Invalid credentials");
      }

      const data = await response.json();

      if (data.token) {
        localStorage.setItem("authToken", data.token);
      }

      message.success(`Welcome back, ${values.email}!`);
      //Todo: Redirect to dashboard
    } catch (err: any) {
      message.error(err.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Content
        style={{
          flex: 1,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: token.colorBgLayout,
        }}
      >
        <div
          style={{
            width: 460,
            padding: "48px 40px",
            borderRadius: 16,
            boxShadow: "0 8px 24px rgba(0,0,0,0.12)",
            backgroundColor: token.colorBgContainer,
          }}
        >
          <Title level={2} style={{ textAlign: "center", marginBottom: 8 }}>
            Welcome Back
          </Title>
          <Text
            type="secondary"
            style={{ display: "block", textAlign: "center", marginBottom: 32 }}
          >
            Sign in to continue to your dashboard
          </Text>

          <Form
            name="login"
            layout="vertical"
            onFinish={onFinish}
            requiredMark={false}
          >
            <Form.Item
              name="email"
              label="Email"
              rules={[
                { required: true, message: "Please enter your email" },
                { type: "email", message: "Invalid email address" },
              ]}
            >
              <Input
                prefix={<UserOutlined />}
                placeholder="you@example.com"
                size="large"
              />
            </Form.Item>

            <Form.Item
              name="password"
              label="Password"
              rules={[
                { required: true, message: "Please enter your password" },
              ]}
            >
              <Input.Password
                prefix={<LockOutlined />}
                placeholder="••••••••"
                size="large"
              />
            </Form.Item>

            <Form.Item>
              <Button
                type="primary"
                htmlType="submit"
                size="large"
                block
                loading={loading}
                icon={<LoginOutlined />}
              >
                Sign In
              </Button>
            </Form.Item>
          </Form>

          <Text
            type="secondary"
            style={{ display: "block", textAlign: "center", marginTop: 24 }}
          >
            Don't have an account? <a href="/register">Register now</a>
          </Text>
        </div>
      </Content>
    </Layout>
  );
}
