package com.example.backfire.decoy

import org.json.JSONObject
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Test

/** The phone's own extractor rules (no network). Values must match the server decoy's (decoy/tests/test_core.py). */
class ExtractorTest {
    private fun v(json: String) = Extractor.validate(JSONObject(json))?.toString()

    @Test fun spokenEmailHandle() = assertEquals(
        """{"kind":"payment_handle","rail":"zelle","id":"refunds.dept@backfire-demo.example"}""",
        v("""{"kind":"payment_handle","rail":"Zelle","id":"refunds dot dept at backfire dash demo dot example"}"""))

    @Test fun spokenDomain() = assertEquals("""{"kind":"domain","value":"irs-payments.com"}""",
        v("""{"kind":"domain","value":"irs dash payments dot com"}"""))

    @Test fun phone() {
        assertEquals("""{"kind":"callback_phone","value":"+18005550199"}""", v("""{"kind":"callback_phone","value":"1 (800) 555-0199"}"""))
        assertNull(v("""{"kind":"callback_phone","value":"555-0199"}"""))
    }

    @Test fun btcChecksum() {
        assertEquals("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
            Extractor.validate(JSONObject("""{"kind":"wallet","chain":"BTC","addr":"1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}"""))!!.getString("addr"))
        assertNull(v("""{"kind":"wallet","chain":"BTC","addr":"1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNb"}"""))
    }

    @Test fun emptyBrandRejected() = assertNull(v("""{"kind":"gift_card_brand","value":""}"""))

    @Test fun personaCardFailsLuhn() = assertFalse(Persona.luhnOk(Persona("c1").raw["card_number"]!!))
}
