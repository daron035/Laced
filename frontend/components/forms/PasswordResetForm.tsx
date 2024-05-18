"use client";

import { Form } from "@/components/forms";
import { useResetPassword } from "@/hooks";

export default function PasswordResetForm() {
  const { email, isLoading, onChange, onSubmit } = useResetPassword();

  const config = [
    {
      labelText: "Email address",
      labelId: "email",
      type: "email",
      value: email,
      required: true,
    },
  ];

  return (
    <Form
      config={config}
      isLoading={isLoading}
      btnText="CHANGE PASSWORD"
      onChange={onChange}
      onSubmit={onSubmit}
    />
  );
}
