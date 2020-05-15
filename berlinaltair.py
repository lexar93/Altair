import sys
import pandas as pd
import altair as alt

if sys.version_info[0] < 3:
    reload(sys) # noqa: F821 pylint:disable=undefined-variable
    sys.setdefaultencoding("utf-8")





@st.cache
def load_data():
   df= pd.read_csv('berlinplan.csv', encoding='utf-8',
   error_bad_lines=False) 
   return df.set_index("BEZIRK")


data = load_data()

districts = st.multiselect(
    "Choose countries", list(df.index), ["Mitte", "Spandau"]
)


data = df.loc[districts]
st.write("Berlin Districts", data.sort_index())


chart = alt.Chart(berlinplan).mark_point(filled=True).encode(
    alt.X('activity:Q', scale=alt.Scale(zero=False)),
    alt.Y('habitants:Q', scale=alt.Scale(zero=False)),
    alt.Size('surface:Q'),
    alt.Color('BEZIRK:N'),
    alt.OpacityValue(0.5),
    tooltip = [alt.Tooltip('BEZIRK:N'),
               alt.Tooltip('activity:Q'),
               alt.Tooltip('habitants:Q'),
               alt.Tooltip('surface:Q')
              ]
  )

st.altair_chart(chart, use_container_width=True)