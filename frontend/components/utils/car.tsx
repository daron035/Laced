import { getSessionID } from "./session";
import { cookies } from "next/headers";
import { headers } from "next/headers";

export enum Path {
  related_products = "product/related_products/",
  trending_products = "product/trending_products/",
}

export async function getData(type: Path) {
  let url = "";
  switch (type) {
    case Path.related_products:
      url = Path.related_products;
      return await getD(url);
    case Path.trending_products:
      url = Path.trending_products;
      return await getD(url);
    default:
      throw new Error(`Unhandled type: ${type}`);
  }
}

export async function getD(url: string) {
  // const sessionid = getSessionID();

  const existingCookies = cookies().toString();
  let sessionID = cookies().has("sessionid")
    ? cookies().get("sessionid")?.toString()
    : headers().get("sessionid")?.toString();

  const res = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/${url}`, {
    cache: "no-store",
    headers: { Cookie: `${existingCookies}; ${sessionID}` },
    // headers: {
    //   // Authorization: `JWT ${cookies.access}`,
    //   Cookie: sessionid || "",
    //   // Cookie: `sessionid=${sessionid}`,
    // },
    credentials: "include",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return await res.json();
}
