import {useState} from "react";
import {getHtml, getText, getSelectorsData, Mode} from "../services/api";
import {Select, Button, Input, Card} from "@mui/material";

export default function ScrapeComp(){
    const [url, setUrl] = useState("");
    const [mode, setMode] = useState<Mode>(Mode.HTML);
    const [selector, setSelector] = useState("");
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleScrape = async () => {
        if (!url.trim()) {
            setError("Please enter a valid URL.");
            return;
        }

        setLoading(true);
        setError(null);
        setData(null);

        try {
            let response;
            if (mode === Mode.HTML) {
                response = await getHtml(url);
            } else if (mode === Mode.TEXT) {
                response = await getText(url);
            } else if (mode === Mode.SELECTOR) {
                if (!selector.trim()) {
                    setError("Selector is required for this mode.");
                    setLoading(false);
                    return;
                }
                response = await getSelectorsData(url, selector);
            }
            setData(response);
        } catch (err) {
            setError("Error fetching data. Please try again.");
        } finally {
            setLoading(false);
        }
    };
    return(
        
    )

};
            

