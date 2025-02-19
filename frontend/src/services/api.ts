import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";


export enum Mode {
    HTML = "html",
    TEXT = "text",
    SELECTOR = "selector",
}

export const getHtml = async (url: string) => {
    try{
        const response = await axios.get(`${API_BASE_URL}/scrape/get-html`, {
            params: {url},
        });
        return response.data
    } catch(error: any) {
        console.error("Error Fetching HTML", error.response?.data || error.message);
        throw error
    }
};

export const getText = async (url: string) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/scrape/get-text-from-html`, {
            params: {url}
        });
        return response.data
    } catch (error: any) {
        console.error("Error fetching Text From HTML", error.response?.data || error.message);
        throw error
    }
};

export const getSelectorsData = async (url : string, selector: string) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/scrape/get-specific-selector`, {
            params: {url, selector}
        });
        return response.data
    } catch (error: any) {
        console.error("Error fetching data from specific selector", error.response?.data || error.message);
        throw error
    }
};


export const customScrape = async (url : string, mode: Mode, selector?: string ) => {
    try {
        const params: Record<string, string> = {url, mode};
        if (mode === Mode.SELECTOR && selector){
            params.selector = selector;
        }

        const response = await axios.get(`${API_BASE_URL}/scrape/get-html-text-selector-text`, {params});
        return response.data
    } catch(error: any) {
        if (axios.isAxiosError(error)) {
            console.error("Error fetching HTML/Text/Selector data:", error.response?.data || error.message);
        } else {
            console.error("Unexpected error:", error);
        }
        throw error;
    }
};