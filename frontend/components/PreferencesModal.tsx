import { HiOutlineChevronDown } from "react-icons/hi";
import { GeneralButton } from "@/components/common";
import { useEscapeKey, useOutsideClick } from "@/hooks";
import { useState, useRef, useEffect } from "react";

interface Props {
  callbackClose: () => void;
  preferences: any;
}

export default function PreferencesModal({
  callbackClose,
  preferences,
}: Props) {
  const [selectedPref, setSelectedPref] = useState<{
    country: string;
    currency: string;
  }>({
    country: "",
    currency: "",
  });

  // const sendYes = () => callbackClose();
  // const sendNo = () => callbackClose();

  useEscapeKey(callbackClose);

  const ref = useRef(null);
  // useOutsideClick(sendNo, ref);
  useOutsideClick(callbackClose, ref);

  useEffect(() => {
    setSelectedPref({
      country: preferences.country_iso,
      currency: preferences.currency_iso,
    });
  }, [preferences]);

  function handleChangePref(event: React.ChangeEvent<HTMLSelectElement>) {
    setSelectedPref({
      ...selectedPref,
      [event.target.name]: event.target.value,
    });
  }

  return (
    <div
      className={`fixed left-0 top-0 z-10 w-full h-full bg-black bg-opacity-50
                  flex items-center justify-center`}
    >
      <div
        className="flex flex-col max-w-md divide-y bg-white text-black"
        ref={ref}
      >
        <header className="p-6 text-center">
          <h2 className="text-xl mb-1">Change your settings</h2>
          <p className="text-sm font-light">
            Choose your language & your preferred currency below
          </p>
        </header>
        <div className="p-6 flex flex-col">
          <label htmlFor="region-select" className="mb-2">
            Region
          </label>
          <div className="relative flex items-center border border-gray-200 hover:border-gray-400 transition duration-200 ease-in-out">
            <select
              name="country"
              id="region-select"
              value={selectedPref.country}
              // onChange={handleChangePref}
              onChange={(e) => handleChangePref(e)}
              className="relative w-full h-10 outline-none appearance-none pl-4 pr-8"
            >
              <option value="US">United States</option>
              <option value="AU">Australia</option>
              <option value="CA">Canada</option>
              <option value="FR">France</option>
              <option value="DE">Germany</option>
              <option value="HK">Hong Kong SAR</option>
              <option value="IT">Italy</option>
              <option value="JP">Japan</option>
              <option value="SG">Singapore</option>
              <option value="AE">United Arab Emirates</option>
              <option value="GB">United Kingdom</option>
              <option value="AL">Albania</option>
              <option value="DZ">Algeria</option>
              <option value="AS">American Samoa</option>
              <option value="AD">Andorra</option>
              <option value="AO">Angola</option>
              <option value="AI">Anguilla</option>
              <option value="AG">Antigua &amp; Barbuda</option>
              <option value="AR">Argentina</option>
              <option value="AM">Armenia</option>
              <option value="AW">Aruba</option>
              <option value="AU">Australia</option>
              <option value="AT">Austria</option>
              <option value="AZ">Azerbaijan</option>
              <option value="BS">Bahamas</option>
              <option value="BH">Bahrain</option>
              <option value="BB">Barbados</option>
              <option value="BE">Belgium</option>
              <option value="BZ">Belize</option>
              <option value="BJ">Benin</option>
              <option value="BM">Bermuda</option>
              <option value="BT">Bhutan</option>
              <option value="BO">Bolivia</option>
              <option value="BA">Bosnia</option>
              <option value="BW">Botswana</option>
              <option value="BR">Brazil</option>
              <option value="VG">British Virgin Isles</option>
              <option value="BN">Brunei</option>
              <option value="BG">Bulgaria</option>
              <option value="BF">Burkina Faso</option>
              <option value="BI">Burundi</option>
              <option value="KH">Cambodia</option>
              <option value="CM">Cameroon</option>
              <option value="CA">Canada</option>
              <option value="IC">Canary Islands</option>
              <option value="CV">Cape Verde</option>
              <option value="KY">Cayman Islands</option>
              <option value="TD">Chad</option>
              <option value="CL">Chile</option>
              <option value="CN">China, Mainland</option>
              <option value="CO">Colombia</option>
              <option value="KM">Comoros</option>
              <option value="CG">Congo</option>
              <option value="CK">Cook Islands</option>
              <option value="CR">Costa Rica</option>
              <option value="HR">Croatia</option>
              <option value="CY">Cyprus</option>
              <option value="CZ">Czech Republic</option>
              <option value="CD">Democratic Republic of Congo</option>
              <option value="DK">Denmark</option>
              <option value="DJ">Djibouti</option>
              <option value="DM">Dominica</option>
              <option value="DO">Dominican Republic</option>
              <option value="EC">Ecuador</option>
              <option value="EG">Egypt</option>
              <option value="SV">El Salvador</option>
              <option value="ER">Eritrea</option>
              <option value="EE">Estonia</option>
              <option value="ET">Ethiopia</option>
              <option value="FO">Faeroe Islands</option>
              <option value="FJ">Fiji</option>
              <option value="FI">Finland</option>
              <option value="FR">France</option>
              <option value="GF">French Guiana</option>
              <option value="PF">French Polynesia</option>
              <option value="GA">Gabon</option>
              <option value="GM">Gambia</option>
              <option value="GE">Georgia</option>
              <option value="DE">Germany</option>
              <option value="GI">Gibraltar</option>
              <option value="GR">Greece</option>
              <option value="GL">Greenland</option>
              <option value="GD">Grenada</option>
              <option value="GP">Guadeloupe</option>
              <option value="GU">Guam</option>
              <option value="GT">Guatemala</option>
              <option value="GG">Guernsey</option>
              <option value="GN">Guinea</option>
              <option value="GW">Guinea-Bissau</option>
              <option value="GY">Guyana</option>
              <option value="HN">Honduras</option>
              <option value="HK">Hong Kong SAR</option>
              <option value="HU">Hungary</option>
              <option value="IS">Iceland</option>
              <option value="IN">India</option>
              <option value="ID">Indonesia</option>
              <option value="IE">Ireland, Republic of</option>
              <option value="IL">Israel</option>
              <option value="IT">Italy</option>
              <option value="CI">Ivory Coast</option>
              <option value="JM">Jamaica</option>
              <option value="JP">Japan</option>
              <option value="JE">Jersey</option>
              <option value="JO">Jordan</option>
              <option value="KZ">Kazakhstan</option>
              <option value="KE">Kenya</option>
              <option value="KI">Kiribati</option>
              <option value="XK">Kosovo</option>
              <option value="KW">Kuwait</option>
              <option value="KG">Kyrgyzstan</option>
              <option value="LA">Laos</option>
              <option value="LV">Latvia</option>
              <option value="LS">Lesotho</option>
              <option value="LI">Liechtenstein</option>
              <option value="LT">Lithuania</option>
              <option value="LU">Luxembourg</option>
              <option value="MO">Macao SAR</option>
              <option value="MK">Macedonia (Fyrom)</option>
              <option value="MG">Madagascar</option>
              <option value="MW">Malawi</option>
              <option value="MY">Malaysia</option>
              <option value="MV">Maldives</option>
              <option value="ML">Mali</option>
              <option value="MT">Malta</option>
              <option value="MH">Marshall Islands</option>
              <option value="MQ">Martinique</option>
              <option value="MR">Mauritania</option>
              <option value="MU">Mauritius</option>
              <option value="YT">Mayotte</option>
              <option value="MX">Mexico</option>
              <option value="FM">Micronesia</option>
              <option value="MD">Moldova</option>
              <option value="MC">Monaco</option>
              <option value="MN">Mongolia</option>
              <option value="ME">Montenegro</option>
              <option value="MS">Montserrat</option>
              <option value="MA">Morocco</option>
              <option value="MZ">Mozambique</option>
              <option value="NA">Namibia</option>
              <option value="NP">Nepal</option>
              <option value="NL">Netherlands</option>
              <option value="NC">New Caledonia</option>
              <option value="NZ">New Zealand</option>
              <option value="NI">Nicaragua</option>
              <option value="NE">Niger</option>
              <option value="NG">Nigeria</option>
              <option value="NF">Norfolk Island</option>
              <option value="MP">Northern Mariana Islands</option>
              <option value="NO">Norway</option>
              <option value="OM">Oman</option>
              <option value="PW">Palau</option>
              <option value="PA">Panama</option>
              <option value="PG">Papua New Guinea</option>
              <option value="PY">Paraguay</option>
              <option value="PE">Peru</option>
              <option value="PH">Philippines</option>
              <option value="PL">Poland</option>
              <option value="PT">Portugal</option>
              <option value="PR">Puerto Rico</option>
              <option value="QA">Qatar</option>
              <option value="RE">Reunion</option>
              <option value="RO">Romania</option>
              <option value="RW">Rwanda</option>
              <option value="RU">Russian Federation</option>
              <option value="WS">Samoa</option>
              <option value="SM">San Marino</option>
              <option value="ST">Sao Tome/Principe</option>
              <option value="SA">Saudi Arabia</option>
              <option value="SN">Senegal</option>
              <option value="RS">Serbia</option>
              <option value="SC">Seychelles</option>
              <option value="SL">Sierra Leone</option>
              <option value="SG">Singapore</option>
              <option value="SK">Slovakia</option>
              <option value="SI">Slovenia</option>
              <option value="SB">Solomon Islands</option>
              <option value="ZA">South Africa</option>
              <option value="KR">South Korea</option>
              <option value="ES">Spain</option>
              <option value="LK">Sri Lanka</option>
              <option value="KN">St. Kitts &amp; Nevis</option>
              <option value="LC">St. Lucia</option>
              <option value="VC">St. Vincent &amp; Grenadines</option>
              <option value="SR">Suriname</option>
              <option value="SZ">Swaziland</option>
              <option value="SE">Sweden</option>
              <option value="CH">Switzerland</option>
              <option value="TW">Taiwan</option>
              <option value="TJ">Tajikistan</option>
              <option value="TZ">Tanzania</option>
              <option value="TH">Thailand</option>
              <option value="TG">Togo</option>
              <option value="TO">Tonga</option>
              <option value="TT">Trinidad &amp; Tobago</option>
              <option value="TN">Tunisia</option>
              <option value="TR">Turkey</option>
              <option value="TM">Turkmenistan</option>
              <option value="TC">Turks &amp; Caicos Islands</option>
              <option value="TV">Tuvalu</option>
              <option value="UG">Uganda</option>
              <option value="AE">United Arab Emirates</option>
              <option value="GB">United Kingdom</option>
              <option value="US">United States</option>
              <option value="UY">Uruguay</option>
              <option value="VI">U.S. Virgin Islands</option>
              <option value="VU">Vanuatu</option>
              <option value="VA">Vatican City State</option>
              <option value="VE">Venezuela</option>
              <option value="VN">Vietnam</option>
              <option value="WF">Wallis &amp; Futuna Islands</option>
              <option value="YE">Yemen</option>
              <option value="ZM">Zambia</option>
              <option value="ZW">Zimbabwe</option>
            </select>
            <HiOutlineChevronDown className="absolute right-2" />
          </div>
          <label htmlFor="language-select" className="mt-3 mb-2">
            Language
          </label>
          <div className="relative flex items-center border border-gray-200 hover:border-gray-400 transition duration-200 ease-in-out">
            <select
              name="language"
              id="language-select"
              className="relative w-full h-10 outline-none appearance-none pl-4 pr-8"
            >
              <option value="en">English</option>
              <option value="it">Italiano</option>
              <option value="de">Deutsch</option>
              <option value="ru">Russian</option>
              <option value="fr">Français</option>
              <option value="ja">日本語</option>
              <option value="zh">简体中文</option>
              <option value="en_gb">English (UK)</option>
              <option value="ko">한국어</option>
              <option value="es_es">Español (ES)</option>
              <option value="es_mx">Español (MX)</option>
              <option value="es_us">Español (US)</option>
              <option value="zh_tw">繁體中文</option>
            </select>
            <HiOutlineChevronDown className="absolute right-2" />
          </div>
          <label htmlFor="currency-select" className="mt-3 mb-2">
            Currency
          </label>
          <div className="relative flex items-center border border-gray-200 hover:border-gray-400 transition duration-200 ease-in-out">
            <select
              name="currency"
              id="currency-select"
              value={selectedPref.currency}
              onChange={(e) => handleChangePref(e)}
              className="relative w-full h-10 outline-none appearance-none pl-4 pr-8"
            >
              <option value="AUD">$ AUD</option>
              <option value="CAD">$ CAD</option>
              <option value="CHF">CHF</option>
              <option value="EUR">€ EUR</option>
              <option value="GBP">£ GBP</option>
              <option value="RUB">₽ RUB</option>
              <option value="HKD">$ HKD</option>
              <option value="JPY">¥ JPY</option>
              <option value="KRW">₩ KRW</option>
              <option value="MXN">$ MXN</option>
              <option value="NZD">$ NZD</option>
              <option value="SGD">$ SGD</option>
              <option value="USD">$ USD</option>
            </select>
            <HiOutlineChevronDown className="absolute right-2" />
          </div>
        </div>
        <footer className="flex justify-between py-3 px-6">
          <GeneralButton
            sm
            action="white"
            title="Cancel"
            // onClick={() => callbackClose()}
            onClick={callbackClose}
          />
          <GeneralButton
            sm
            action="black"
            title="Save Changes"
            // onClick={() => callbackClose()}
            onClick={callbackClose}
          />
        </footer>
      </div>
    </div>
  );
}
