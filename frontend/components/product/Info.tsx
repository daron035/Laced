import Actions from "../product/Actions";
import Accordion from "../product/Accordion";
import Details from "./Details";
import Header from "../product/Header";

import { Size } from "@/utils/countries.utils";

type Props = {
  data: any;
  sizeData: Size[];
};

export default function Info({ data, sizeData }: Props) {
  return (
    <div className="shrink-0 w-[420px] pt-[32px]">
      <Header brand={data.brand} sku={data.sku} name={data.name} />
      <Actions
        data_matrix={sizeData}
        product_id={data.id}
        currency_iso={data.currency_iso}
        currency_symbol={data.currency_symbol}
      />
      <Accordion />
      <Details
        brand={data.brand}
        categories={data.categories}
        colour={data.colour}
        description={data.description}
        year_released={data.year_released}
      />
    </div>
  );
}
