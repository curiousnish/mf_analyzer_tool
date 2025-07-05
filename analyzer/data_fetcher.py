from mftool import Mftool

class MutualFundAPI:
    def __init__(self):
        self.mf = Mftool()

    def get_all_schemes(self):
        """Fetches all mutual fund schemes."""
        try:
            schemes = self.mf.get_scheme_codes()
            return schemes
        except Exception as e:
            print(f"Error fetching all schemes: {e}")
            return {}

    def get_scheme_details(self, scheme_code):
        """Fetches details for a given scheme code."""
        try:
            return self.mf.get_scheme_details(scheme_code)
        except Exception as e:
            print(f"Error fetching scheme details for {scheme_code}: {e}")
            return None

    def get_historical_nav(self, scheme_code):
        """Fetches historical NAV data for a given scheme code."""
        try:
            historical_data = self.mf.get_scheme_historical_nav(scheme_code)
            # print(f"Raw historical NAV data for {scheme_code}: {historical_data}") # Removed for cleaner output
            return historical_data
        except Exception as e:
            print(f"Error fetching historical NAV for {scheme_code}: {e}")
            return None

# Instantiate the API for use in other modules
mf_api = MutualFundAPI()

if __name__ == "__main__":
    # Example usage
    all_schemes = mf_api.get_all_schemes()
    # print(f"Total schemes fetched: {len(all_schemes)} schemes")
    selected_scheme = "130502"
    if selected_scheme in all_schemes:
        # scheme_code = all_schemes[selected_scheme]
        scheme_details = mf_api.get_scheme_details(selected_scheme)
        historical_nav = mf_api.get_historical_nav(selected_scheme)

        print(f"Scheme Code: {selected_scheme}")
        print(f"Scheme Details: {scheme_details}")
        print(f"Historical NAV Data: {historical_nav}...")
    else:
        print(f"Scheme '{selected_scheme}' not found in the fetched schemes.")
    # print(f"Sample scheme: {list(all_schemes.items())[0]}")
