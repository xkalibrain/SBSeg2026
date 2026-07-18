export type ScansAvailable = "whatweb" | "reverseDNS" | "subDNS" | "whoIs" | "banner" | "directoryScan" | "ports"

export type ScanState = {
  name: ScansAvailable
  isLoading: boolean
  result: string
}
