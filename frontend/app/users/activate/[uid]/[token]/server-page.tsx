import { redirect } from "next/navigation";

interface Props {
  params: {
    uid: string;
    token: string;
  };
}

async function activate(uid: string, token: string) {
  const res = await fetch("http://localhost:8000/api/auth/users/activation/", {
    method: "POST",
    body: JSON.stringify({ uid, token }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (!res.ok) return undefined;
  if (res.ok && res.status === 204) return true;
  return res.json();
}

export default async function Profile({ params }: Props) {
  const activated = await activate(params.uid, params.token);
  if (activated) {
    redirect("/users/sign_in");
  } else {
    redirect("/");
  }
}
