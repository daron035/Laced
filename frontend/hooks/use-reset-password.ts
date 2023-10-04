import { useResetPasswordMutation } from "@/redux/features/authApiSlice";
import { ChangeEvent, FormEvent, useState } from "react";
import toast from "react-hot-toast";

export default function useResetPassword() {
  const [resetPassword, { isLoading }] = useResetPasswordMutation();

  const [email, setEmail] = useState("");

  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    resetPassword(email)
      .unwrap()
      .then(() => {
        toast.success("Request sent, check your email for reset link");
      })
      .catch(() => {
        toast.error("Failed to send request");
      });
  };

  return {
    email,
    isLoading,
    onChange,
    onSubmit,
  };
}
