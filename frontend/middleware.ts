import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export async function middleware(request: NextRequest) {
  const response = NextResponse.next();

  if (!request.cookies.has("sessionid")) {
    const requestIPinfo = await fetch(
      "https://ipinfo.io/json?token=7c77d9047c4e08",
    );
    const jsonResponse = await requestIPinfo.json();

    const getSessionID = await fetch(
      `${process.env.NEXT_PUBLIC_HOST}/api/cookie/`,
      {
        headers: {
          Cookie: `country=${jsonResponse.country}`,
        },
      },
    );

    const cookieHeader = getSessionID.headers.get("Set-Cookie");
    if (cookieHeader) {
      const cookies = cookieHeader.split(", ");
      cookies.forEach((cookie) => {
        const [name, value] = cookie.split(";")[0].split("=");
        if (name.trim() === "sessionid") {
          response.cookies.set("sessionid", value);
          response.headers.set("sessionid", value);
        }
      });
    }
  }
  return response;
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
