import { SocialButtons } from "@/components/common";
import { LoginForm } from "@/components/forms";
import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Login",
  description: "Login page",
};

export default function Page() {
  return (
    <div className="w-[560px] mx-auto px-[40px] pt-[80px] pb-[100px]">
      <h1 className="mb-[40px] text-[#101010] uppercase font-medium text-4xl tracking-wide subpixel-antialiased">
        Log In
      </h1>

      <LoginForm />

      <SocialButtons />

      <p className="text-sm text-[#101010] tracking-tight font-semibold underline">
        <Link
          className="pr-[10px] mr-[10px] border-r-[1px]"
          href="/users/sign_up"
        >
          Sign Up
        </Link>
        <Link
          className="pr-[10px] mr-[10px] border-r-[1px]"
          href="/users/password-reset"
        >
          Forgot Your Password?
        </Link>
        <Link href="#">Didn&#39;t Receive Confimation Instructions?</Link>
      </p>
    </div>
  );
}
