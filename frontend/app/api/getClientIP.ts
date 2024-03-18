import { NextRequest, NextResponse } from "next/server";
// import requestIp from "request-ip";

// export default function handler(req: NextRequest, res: NextResponse) {
export async function GET(req: NextRequest, res: NextResponse) {
  const requestIp = require("request-ip");
  const detectedIp = requestIp.getClientIp(req);
  console.log(detectedIp);
  // const clientIP =
  //   req.headers["x-forwarded-for"] || req.connection.remoteAddress;
  // res.status(200).json({ clientIP });
  // res.status(200).json({ detectedIp });
  return NextResponse.json({ message: "Hello" });
}
