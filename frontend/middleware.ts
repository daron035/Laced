import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { headers } from "next/headers";

export function middleware(request: NextRequest) {
  const allCookies = request.cookies.getAll();
  // console.log(allCookies);
  const response = NextResponse.next();
  // response.cookies.set("myCookie", "123");
  // console.log("3");
  return response;
}
