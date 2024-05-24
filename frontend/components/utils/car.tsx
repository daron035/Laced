// import { getSessionID } from "./session";
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
      return await getRequest(url);
    case Path.trending_products:
      url = Path.trending_products;
      return await getRequest(url);
    default:
      throw new Error(`Unhandled type: ${type}`);
  }
}

export async function getRequest(url: string) {
  const existingCookies = cookies().toString();

  // Получаем значения заголовков 'lang' и 'country'
  const langHeader = headers().get("lang")?.toString() || "";
  const countryHeader = headers().get("country")?.toString() || "";
  const sessionidHeader = headers().get("sessionid")?.toString() || "";

  // Формируем строку Cookie для заголовков запроса
  const cookieHeader = `${existingCookies}${langHeader ? `; lang=${langHeader}` : ""}${countryHeader ? `; country=${countryHeader}` : ""}${sessionidHeader ? `; sessionid=${sessionidHeader}` : ""}`;

  const res = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/${url}`, {
    cache: "no-store",
    headers: {
      Cookie: cookieHeader,
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return await res.json();
}
