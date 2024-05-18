import Carousel from "@/components/common/Carousel";
import Sl from "@/components/common/Sl";
import { getSession } from "@/session";
import { Path, getData } from "@/utils/car";

import { cookies } from "next/headers";
import { headers } from "next/headers";
import { getIronSession } from "iron-session";

export default async function Page() {
  // const session = await getSession();
  // const data = await getData("related_products");
  const a = cookies().get("sessionid");
  const b = headers().get("sessionid");
  // const headersList = headers()
  // const middlewareSet = headersList.get('middlewareSet')

  // const c = a?.value
  let c;
  if (!a) {
    c = b + "                             header";
  } else {
    c = a.value + "                             cookie";
  }
  // const data = await getData("related_products");
  const data = await getData(Path.related_products);
  // const data = await getData(.related);
  // const a = cookies().getAll()

  // console.log();
  // console.log();
  // console.log();
  // console.log();
  // console.log("[][][][][][][][][]", c);
  // // console.log(session);
  // console.log();
  // console.log();
  // console.log();
  // console.log();

  return (
    <div className="">
      <Sl />
      {/* <p>asdf {a ? a : "23"}</p> */}
      {/* <p>asdf {a ? a.value : "23"}</p> */}
      {/* <p>asdf {c}</p>
      <p>middlewareSet: {JSON.stringify(middlewareSet)}</p>   */}
      {/* <p>asdf {a && a[0].value}</p> */}
      {/* <p>asdf: {session?.username}</p> */}
      <div className="max-w-[1162px] mx-auto">
        {data && <Carousel data={data} title="related products" />}
      </div>
    </div>
  );
}
