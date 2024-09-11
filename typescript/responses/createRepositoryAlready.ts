export interface TopLevel {
    message:           string;
    errors:            Error[];
    documentation_url: string;
    status:            string;
}

export interface Error {
    resource: string;
    code:     string;
    field:    string;
    message:  string;
}
